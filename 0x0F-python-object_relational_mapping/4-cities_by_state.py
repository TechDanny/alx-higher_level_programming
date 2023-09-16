#!/usr/bin/python3
"""
List all cities from Database
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states
                ON states.id = cities.state_id
                ORDER BY cities.id""")
    all_data = cur.fetchall()

    for dt in all_data:
        print(dt)
    cur.close()
    conn.close()
