import typer
from typing_extensions import Annotated

from votedb.elections.actions import insert

app = typer.Typer()


@app.command()
def create(name: Annotated[str, typer.Option(prompt=True)]):
    print(f"Created {name}")
    insert(name)
