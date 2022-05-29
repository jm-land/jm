import sys

import click
import llvmlite
import rply

from . import __version__
from .lexing import Tokenizer


# TODO: Compile Command
@click.group()
@click.version_option(
    __version__,
    '--version',
    '-v',
    message=f'nextc: %(version)s\nllvmlite: {llvmlite.__version__}\nrply: {rply.__version__}\nclick: {click.__version__}\npython: {sys.version}',
)
def cli():
    pass


@cli.command('lex')
@click.option('-f', '--file', 'file', required=True, help='The File to Lex')
def lex_code(file: str):
    with open(file) as f:
        buffer = f.read()
        tokenizer = Tokenizer(code=buffer, filename=file)
        tokens = tokenizer.start()
        print(str(tokens), file=sys.stderr)


if __name__ == '__main__':
    cli()
