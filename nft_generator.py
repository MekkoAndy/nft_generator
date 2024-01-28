import click


@click.command()
@click.option("--remove-user")
def cli(remove_user):
    if click.confirm(f"Remove user '{remove_user}'?"):
        click.echo(f"User {remove_user} successfully removed!")
    else:
        click.echo("Aborted!")


# pseudocode
def initialization(path):
    pass