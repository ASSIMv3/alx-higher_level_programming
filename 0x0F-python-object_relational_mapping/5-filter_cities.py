#!/usr/bin/python3
"""takes in the name of a state as an argument and
lists all cities of that state, using the database"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    db_connect = db.connect(host="localhost", port=3306, user=argv[1],
                            passwd=argv[2], db=argv[3])
    db_connect.cursor() = db_cursor:
        db_cursor.execute("SELECT cities.name \
                    FROM cities \
                    INNER JOIN states ON \
                    states.id=cities.state_id \
                    AND states.name=%s; \
                    ", {'state_name': argv[4]})
    rows = db_cursor.fetchall()
    if rows is not None:
        print(", ".join([row[1] for row in rows]))
