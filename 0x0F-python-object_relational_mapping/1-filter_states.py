#!/usr/bin/python3
"""lists all states with a name starting with N from the database"""

import MySQLdb as db
from sys import argv
if __name__ == '__main__':
    db_connect = db.connect(host="localhost", port=3306, user=argv[1],
                            passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    rows = db_cursor.fetchall()
    for row in rows:
        print(row)
