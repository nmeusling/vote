import typer
from rich import print
from typing_extensions import Annotated

app = typer.Typer(no_args_is_help=True)


@app.command()
def create(election_name: Annotated[str, typer.Option(prompt=True)]):
    print("Create an election")
    if election_name:
        print(f"Created {election_name}")
    else:
        print("Please enter election name: ")


@app.command()
def view():
    print("View and election")


if __name__ == "__main__":
    app()
