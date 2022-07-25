# importing click
import click

@click.command()
def main():
	click.echo("This cli is built with click. ")

if __name__=="__main__":
	main()

