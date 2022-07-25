# The example creates a commanda that outputs the message
import click



@click.command()
@click.argument("name",default="guest")
def hello(name):
    click.echo(f"Hellos {name}")
    
if __name__=="__main__":
    hello()
    
