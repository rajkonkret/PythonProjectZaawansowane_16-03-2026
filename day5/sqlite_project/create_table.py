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

    sql_create_tasks_table = """
        CREATE TABLE IF NOT EXISTS tasks(
        id integer PRIMARY KEY,
        name text NOT NULL,
        priority INTEGER,
        status_id integer NOT NULL,
        project_id integer NOT NULL,
        begin_date text,
        end_date text,
        FOREIGN KEY (project_id) REFERENCES projects(id)
        );
        """

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_projects_table)
        create_table(conn, sql_create_tasks_table)
    else:
        print("Błąd podłączenia z bazą danych")
