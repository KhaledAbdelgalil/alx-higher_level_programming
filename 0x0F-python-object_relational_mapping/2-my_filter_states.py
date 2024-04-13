#!/usr/bin/python3
"""
list all states in the given database started by N
"""
import sys
import MySQLdb

if __name__ == '__main__':
    # Open database connection
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{}%' \
                   ORDER BY id;".format(sys.argv[4]))
    states = cursor.fetchall()
    for state in states:
        print(state)
