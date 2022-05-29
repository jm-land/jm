import click
import nextc


# TODO: Compiling, Project Creation, Running, etc
@click.group()
@click.version_option(
    None,
    '--version',
    '-v',
    message=f'parcel: %(version)s\nnextc: {nextc.__version__}',
)
def version():
    pass


if __name__ == '__main__':
    version()
