import typer

app = typer.Typer()


@app.command()
def view():
    print("View an election")
    # print(view_elections())
