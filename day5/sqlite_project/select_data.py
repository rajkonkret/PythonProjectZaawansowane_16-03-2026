from conn import create_connection


def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()
    for row in rows:
        print(row)


def select_all_projects(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM projects")

    rows = cur.fetchall()
    for row in rows:
        print(row)


def select():
    database = "mojabaza1.db"
    conn = create_connection(database)

    with conn:
        print("1. Wszystkie zadania: ")
        select_all_tasks(conn)

        print("2. Wszystkie zadania: ")
        select_all_tasks(conn)
