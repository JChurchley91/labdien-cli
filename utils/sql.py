import sqlite3
from sqlite3 import Error


def read_sql_query(query_path: str) -> str:
    """

    :param query_path:
    :return:
    """
    try:
        fd = open(f"./queries/{query_path}", "r")
        sql_file = fd.read()
        fd.close()
        return sql_file
    except Error as error:
        raise error


def database_conn() -> sqlite3.Connection:
    """

    :return:
    """
    try:
        conn = sqlite3.connect("db/labdien")
        return conn
    except Error as error:
        raise error


def create_user_table(conn: sqlite3.Connection) -> None:
    """
    create user table if it doesn't already exist.
    :return: none.
    """
    try:
        cursor = conn.cursor()
        query = read_sql_query(query_path="users.sql")
        cursor.execute(query)
    except Error as error:
        raise error


def create_user_login_table(conn: sqlite3.Connection) -> None:
    """
    create user login table if it doesn't already exist.
    :return: none.
    """
    try:
        cursor = conn.cursor()
        query = read_sql_query(query_path="user_login.sql")
        cursor.execute(query)
    except Error as error:
        raise error


def get_users(conn: sqlite3.Connection) -> list:
    """

    :param conn:
    :return:
    """
    try:
        cursor = conn.cursor()
        query = read_sql_query(query_path="get_users.sql")
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Error as error:
        raise error


def get_user_id(conn: sqlite3.Connection, username: str, password: str) -> int:
    """

    :param conn:
    :param username:
    :param password:
    :return:
    """
    try:
        cursor = conn.cursor()
        query = read_sql_query(query_path="get_user_id.sql")
        cursor.execute(query, (username, password))
        row = cursor.fetchone()
        return row[0]
    except Error as error:
        raise error


def insert_user_login(conn: sqlite3.Connection, user_id: int) -> None:
    """

    :param conn:
    :param user_id:
    :return:
    """
    try:
        cursor = conn.cursor()
        query = read_sql_query(query_path="insert_user_login.sql")
        cursor.execute(query, [user_id])
        conn.commit()
    except Error as error:
        raise error


def create_user(conn: sqlite3.Connection, username: str, password: str) -> None:
    """

    :param conn:
    :param username:
    :param password:
    :return:
    """
    try:
        cursor = conn.cursor()
        query = read_sql_query(query_path="insert_user.sql")
        cursor.execute(query, (username, password))
        conn.commit()
    except Error as error:
        raise error
