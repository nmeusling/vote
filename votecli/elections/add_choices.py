from typing import List

import typer
from typing_extensions import Annotated

from votedb.elections.actions import (
    add_options_to_election,
    view_election_options,
    view_elections,
)

app = typer.Typer()


@app.command()
def add_options(
    name: Annotated[str, typer.Argument()],
    options: Annotated[
        List[str],
        typer.Argument(
            help="Options to add to election",
            show_default=True,
        ),
    ],
):
    add_options_to_election(name, options)
    print(name)
    print(options)
    print(view_election_options(name))
