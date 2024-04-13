#!/usr/bin/python3
"""
List all cities from a database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities INNER JOIN states \
                   ON cities.state_id = states.id AND\
                   states.name = %s \
                   ORDER BY cities.id;", (sys.argv[4],))
    records = cursor.fetchall()
    print(", ".join([record[0] for record in records]))
