import click
@click.command()
@click.argument("name",default="guest")
def hello(name):
    click.echo(f"hello {name}")

if __name__=="__main__":
    hello()
    
