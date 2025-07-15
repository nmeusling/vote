import typer

from .create import app as create_app
from .delete import app as delete_app
from .view import app as view_app

app = typer.Typer()

app.add_typer(create_app)
app.add_typer(delete_app)
app.add_typer(view_app)
