from sqlite3 import Error
from conn import create_connection


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def cr():
    database = "mojabaza1.db"

    sql_create_projects_table = """
    CREATE TABLE IF NOT EXISTS projects(
    id integer PRIMARY KEY,
    name text NOT NULL,
    begin_date text,
    end_date text
    );
    """
