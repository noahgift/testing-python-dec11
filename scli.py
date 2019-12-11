#!/usr/bin/env python
import click
import glob 
from mylib import ftypes


@click.command()
@click.option('--path', prompt='Path to search for files',
              help='This is the path to search for files: /tmp')
def search(path):
    
    patt = ftypes.py_pattern()
    click.echo(f"Search for pattern: {patt}")
    results = glob.glob(f"{path}/{patt}")
    click.echo(click.style('Found Matches:', fg='red'))
    for result in results:
        click.echo(click.style(f'{result}', bg='blue', fg='white')) 
if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    search()