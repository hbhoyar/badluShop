import psycopg2
from utils.config import config

def connect():
    try:
        conn = psycopg2.connect(**config)     # use config package for connection params
    except Exception as e:
        print("Connection Error:", e)
        exit(1)

    return conn


def exec_query(conn, sql):
    """Execute sql query. Return header and rows"""
    cursor = conn.cursor()
    cursor.execute(sql)
    header = list(map(lambda x: x[0], cursor.description))
    rows = cursor.fetchall()
    cursor.close()
    return (header, rows)


def exec_query1(conn, sql):
    """Execute sql query. Return header and rows"""
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()

if __name__ == "__main__":
    from sys import argv
    import config

    query = argv[1]
    try:
        conn = connect()
        (header, rows) = exec_query(conn, query)
        print(",".join([str(i) for i in header]))
        for r in rows:
            print(",".join([str(i) for i in r]))
    except psycopg2.errors.Error as err:
        print("ERROR %%%%%%%%%%%%%%%% \n", err)
