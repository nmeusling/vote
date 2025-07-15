import typer

app = typer.Typer()


@app.command()
def delete():
    print("Delete an election")
    # print(view_elections())
