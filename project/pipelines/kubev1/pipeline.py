import click
import os
import kfp
from kfp import dsl


def data_op():
    return dsl.ContainerOp(
        name='data pipeline',
        image='registry-vpc.cn-beijing.aliyuncs.com/he-test/kube-pipelines:latest',
        command=['bash', '-c'],
        arguments=["./entry_point.sh --entry /kubev1/pipeline_data.py --path_remote oss://peng/dp/"],
        file_outputs={
            'path_dp': '/tmp/path_dp',
            'path_schema': '/tmp/path_schema',
        }
    )


def training_op(path_dp, path_schema):
    return dsl.ContainerOp(
        name='training pipeline',
        image='registry-vpc.cn-beijing.aliyuncs.com/he-test/kube-pipelines:latest',
        command=['bash', '-c'],
        arguments=[
            "./entry_point.sh --entry /kubev1/pipeline_training.py "
            "--path_remote oss://peng/tp/ "
            "--path_dp {path_dp} "
            "--path_schema {path_schema}".format(
                path_dp=path_dp,
                path_schema=path_schema)],
        file_outputs={
            'path_tp': '/tmp/result',
        }
    )


@dsl.pipeline(
    name='kubev1 pipeline',
    description='A pipeline with two sequential steps.'
)
def sequential_pipeline(url='gs://ml-pipeline-playground/shakespeare1.txt'):
    """A pipeline with two sequential steps."""

    dp = data_op()
    tp = training_op(dp.outputs['path_dp'], dp.outputs['path_schema'])


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(sequential_pipeline, __file__ + '.yaml')
