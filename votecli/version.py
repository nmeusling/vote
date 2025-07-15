import typer

app = typer.Typer()


@app.command()
def version():
    print("Vote CLI version 0.1")
