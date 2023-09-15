#!/usr/bin/python3
"""
lists all states from database
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()

    for r in query_rows:
        print(r)
    cur.close()
    conn.close()
