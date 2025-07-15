import typer
from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def create(election_name: Annotated[str, typer.Option(prompt=True)]):
    print(f"Created {election_name}")
    # insert()
