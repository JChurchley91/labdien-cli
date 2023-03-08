import sqlite3
from rich import print
from sqlite3 import Error
from utils.sql import get_users, insert_user_login, get_user_id, create_user


def authenticate_login(conn: sqlite3.Connection, username: str, password: str):
    """

    :param conn:
    :param username:
    :param password:
    :return:
    """
    try:
        for user in get_users(conn):
            if username in user:
                if password in user:
                    return 1
                else:
                    return 2
            else:
                return 3
    except Error as error:
        raise error


def register_user(conn: sqlite3.Connection, username: str, password: str):
    """

    :param conn:
    :param username:
    :param password:
    :return:
    """
    create_user(conn=conn, username=username, password=password)
    register_user_login(conn=conn, username=username, password=password)
    return None


def register_user_login(conn: sqlite3.Connection, username: str, password: str):
    """

    :param conn:
    :param username:
    :param password:
    :return:
    """
    user_id = get_user_id(conn=conn, username=username, password=password)
    insert_user_login(conn=conn, user_id=user_id)
    print("[red]Thanks - you're logged in!")
    return None
