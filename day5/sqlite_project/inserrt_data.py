from conn import create_connection


def create_project(conn, project):
    sql = """
    INSERT INTO projects(name,begin_date,end_date) VALUES(?,?,?);
    """

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def create_task(conn, task):
    sql = """
    INSERT INTO task(name,priority,status_id,project_id,begin_date,end_date) VALUES(?,?,?,?,?,?);
    """

    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid
