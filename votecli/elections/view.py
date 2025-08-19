import typer
from typing_extensions import Annotated

from votedb.elections.actions import (
    view_election_by_name,
    view_elections,
)

app = typer.Typer()


@app.command()
def view(
    name: Annotated[
        str,
        typer.Option(
            help="View existing election by name, by default all will show",
            show_default=True,
        ),
    ] = "",
):
    if name:
        print(view_election_by_name(name))
    else:
        print(view_elections())
