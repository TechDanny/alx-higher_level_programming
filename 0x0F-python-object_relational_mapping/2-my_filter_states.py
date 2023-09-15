#!/usr/bin/python3
"""
script that takes an argument and displays all values
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id
                ASC""".format(argv[4]))
    all_data = cur.fetchall()

    for dt in all_data:
        print(dt)
    cur.close()
    conn.close()
