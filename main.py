import typer
from utils.menu import authenticate_login, register_user
from rich import print
from rich.prompt import Prompt
from utils.sql import (
    database_conn,
    create_user_table,
    create_user_login_table,
    get_user_id,
    insert_user_login,
)

app = typer.Typer()


@app.command()
def labdien():
    """

    :return:
    """
    conn = database_conn()
    create_user_table(conn)
    create_user_login_table(conn)

    print("[red]Labdien![/red]")
    username = Prompt.ask("[red]Enter your username[/red]")
    password = Prompt.ask("[red]And your password[/red]")

    authentication_code = authenticate_login(
        conn=conn, username=username, password=password
    )

    if authentication_code == 1:
        user_id = get_user_id(conn=conn, username=username, password=password)
        insert_user_login(conn=conn, user_id=user_id)
        print("[red]Thanks - you're logged in!")

    elif authentication_code == 2:
        print("[red]Incorrect password supplied.[/red]")

    elif authentication_code == 3:
        register = Prompt.ask(
            "[red]User not found - do you want to register?[/red] (Y/N)"
        )

        if register in ["Y", "N"]:
            if register == "Y":
                register_user(conn=conn, username=username, password=password)
            else:
                print("[red]See you soon![/red]")
        else:
            print("[red]See you soon![/red]")


@app.command()
def manage():
    """

    :return:
    """
    print(f"[bold red]Labdien![/bold red]")


if __name__ == "__main__":
    app()
