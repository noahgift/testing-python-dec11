#!/usr/bin/env python
import click
import glob 
from mylib import lib


@click.command()
def add():
    click.echo(click.style('Runs our library code:', fg='red'))
    result = 1+lib.num()
    click.echo(click.style(f'One + my library code = {result}', bg='blue', fg='white')) 
if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    add()
