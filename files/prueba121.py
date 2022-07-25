#!/usr/bin/python3

import click


@click.command()
@click.option('--caca', is_flag=True, help='message in blue color')
def hello(caca):

    if caca:
        click.secho('Hello there', fg='red')
    else:
        click.secho('Hello there')

 
if __name__ == '__main__':
    hello()

