#!/usr/bin/python3
"""takes in arguments and displays all values in the states table"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    db_connect = db.connect(host="localhost", port=3306, user=argv[1],
                            passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM `states`")
    rows = db_cursor.fetchall()
    for row in rows:
        print(row)
