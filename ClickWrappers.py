import click
import inquirer
from Classes import *

"""
@click.command()
@click.option("--remove-user")
def cli(remove_user):
    if click.confirm(f"Remove user '{remove_user}'?"):
        click.echo(f"User {remove_user} successfully removed!")
    else:
        click.echo("Aborted!")
"""

def inquirer_prompt(options: list, message: str):

    questions = [
        inquirer.List("_",
                    message=message,
                    choices=options,
                    ),
    ]
    answers = inquirer.prompt(questions)
    print(answers["_"])

    return answers["_"]

def inquirer_prompt_bool(message: str):

    questions = [
        inquirer.List("_",
                    message=message,
                    choices=[True, False],
                    ),
    ]
    answers = inquirer.prompt(questions)

    return answers["_"]

inquirer_prompt([e.value for e in RarityType], 'Include rarity score in nfts metadata?')
