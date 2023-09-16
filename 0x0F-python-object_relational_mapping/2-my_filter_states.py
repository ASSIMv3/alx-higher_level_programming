#!/usr/bin/python3
"""takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb as db
from sys import argv
if __name__ == '__main__':
    db_connect = db.connect(host="localhost", port=3306, user=argv[1],
                            passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    rows = db_cursor.fetchall()
    for row in rows:
        print(row)
