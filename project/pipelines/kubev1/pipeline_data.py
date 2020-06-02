import click
import os


@click.command(context_settings=dict(ignore_unknown_options=True, allow_extra_args=True))
@click.option("--path_remote", type=str)
def main(**input_parameters):
    print("data pipeline enter")

    os.system("echo 'this is path_dp result' > /tmp/path_dp")
    os.system("echo 'this is path_schema result' > /tmp/path_schema")

    print("data pipeline exit")


if __name__ == "__main__":
    main()
