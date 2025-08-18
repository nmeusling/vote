import typer

from votedb.elections.actions import create_database

from .elections import app as elections_app
from .version import app as version_app

app = typer.Typer(no_args_is_help=True)
app.add_typer(version_app)
app.add_typer(elections_app, name="elections")


if __name__ == "__main__":
    create_database()
    app()
