import typer
from typing_extensions import Annotated

from votedb.elections.actions import delete_by_name

app = typer.Typer()


@app.command()
def delete(name: Annotated[str, typer.Option()]):
    print("Delete an election")
    delete_by_name(name)
