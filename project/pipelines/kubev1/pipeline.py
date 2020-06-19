import kfp
from kfp import dsl


def data_op():
    return dsl.ContainerOp(
        name='data pipeline',
        image='registry-vpc.cn-beijing.aliyuncs.com/he-test/kube-pipelines:latest',
        arguments=["--entry", "/kubev1/pipeline_data.py",
                   "--path_remote", "oss://dp/"
                   ],
        file_outputs={
            'path_dp': '/tmp/path_dp',
            'path_schema': '/tmp/path_schema',
        }
    )


def data_op2():
    return dsl.ContainerOp(
        name='data pipeline2',
        image='registry-vpc.cn-beijing.aliyuncs.com/he-test/kube-pipelines:latest',
        arguments=["--entry", "/kubev1/pipeline_data.py",
                   "--path_remote", "oss://dp2/"
                   ],
        file_outputs={
            'path_dp': '/tmp/path_dp',
            'path_schema': '/tmp/path_schema',
        }
    )


def training_op(path_dp, path_schema):
    return dsl.ContainerOp(
        name='training pipeline',
        image='registry-vpc.cn-beijing.aliyuncs.com/he-test/kube-pipelines:latest',
        arguments=[
            "--entry", "/kubev1/pipeline_training.py",
            "--path_remote", "oss://peng/tp/",
            "--path_dp", path_dp,
            "--path_schema", path_schema],
        file_outputs={
            'path_tp': '/tmp/result',
        }
    )


@dsl.pipeline(
    name='kubev1 pipeline',
    description='A pipeline with two sequential steps.'
)
def sequential_pipeline(param1="param1"):
    """A pipeline with two sequential steps."""
    # simple run
    dp = data_op()
    tp = training_op(dp.outputs['path_dp'], dp.outputs['path_schema'])

    # run parall
    # dp = data_op()
    # dp2 = data_op()
    # tp = training_op(dp.outputs['path_dp'], dp2.outputs['path_schema'])

    # condition
    # dp = data_op()
    # with dsl.Condition(dp.outputs['path_dp'] == 'this is path_dp res'):
    #     tp = training_op("aaa", dp.outputs['path_schema'])

    # life cycle
    # dp = data_op()
    # with dsl.ExitHandler(dp):
    #     dp2 = data_op()
    #     tp = training_op(dp2.outputs['path_dp'], dp2.outputs['path_schema'])

    print(tp)


if __name__ == '__main__':
    """
    you must run it when kube.config is connect to the kubeflow cluster 
    """
    yaml_file = __file__ + '.yaml'
    kfp.compiler.Compiler().compile(sequential_pipeline, yaml_file)

    client = kfp.Client()
    my_experiment = client.create_experiment(name='demo')
    my_run = client.run_pipeline(my_experiment.id, 'my-pipeline', yaml_file)
