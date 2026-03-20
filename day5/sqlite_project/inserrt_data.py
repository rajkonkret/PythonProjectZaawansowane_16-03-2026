from conn import create_connection

def create_project(conn, project):
    sql = """
    INSERT INTO projects(name,begin_date,end_date) VALUES(?,?,?);
    """

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid