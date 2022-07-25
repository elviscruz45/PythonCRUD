#!/usr/bin/python3

import click


@click.command()
def coloured():
    click.secho('Hello there', fg="red", bold=True)


if __name__ == '__main__':
    coloured()
    
    