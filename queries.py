from connect import get_db_connection


# Pattern q
def get_count(table_name, date=None):
    db_connect = get_db_connection()
    cur = db_connect.cursor()
    if date:
        query = f"SELECT COUNT(*) FROM {table_name} WHERE date(created_at) = %s"
        cur.execute(query, (date,))
    else:
        query = f"SELECT COUNT(*) FROM {table_name}"
        cur.execute(query)
    count = cur.fetchone()[0]
    cur.close()
    db_connect.close()
    return count
