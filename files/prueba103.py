import click

@click.command()
@click.argument('name')
def greeting(name):
	click.echo("Hello, {}".format(name))

if __name__=="__main__":
    greeting()

