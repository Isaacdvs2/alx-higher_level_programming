#!/usr/bin/env python3
""" A script to list all states from the hbtn_0e_0_usa database """

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], host='localhost', port=3306)
    crs = db.cursor()
    crs.execute("SELECT * FROM `states`")
    states = crs.fetchall()

    for state in states:
        print(state)
