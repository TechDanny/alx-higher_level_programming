#!/usr/bin/python3
"""
Takes the name of state as argument and lists all cities
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (argv[4],))

    all_data = cur.fetchall()
    print(", ".join([dt[0] for dt in all_data]))
    cur.close()
    conn.close()
