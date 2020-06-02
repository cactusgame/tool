import click
import os


@click.command(context_settings=dict(ignore_unknown_options=True, allow_extra_args=True))
@click.option("--path_remote", type=str)
@click.option("--path_data", type=str)
@click.option("--path_schema", type=str)
def main(**input_parameters):
    print("training pipeline enter")

    os.system("echo 'training pipeline result' > /tmp/result")

    print("training pipeline exit")


if __name__ == "__main__":
    main()
