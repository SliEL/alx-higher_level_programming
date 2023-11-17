#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
# import MySQLdb
# import sys


# if __name__ == "__main__":
#     db = MySQLdb.connect(host="localhost", user=sys.argv[1],
#                          passwd=sys.argv[2], db=sys.argv[3], port=3306)
#     cur = db.cursor()
#     match = sys.argv[4]
#     cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
#     cur.close()
#     db.close()


import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <match>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    username, password, database, match = sys.argv[1:5]

    # Connect to the database using the context manager
    with MySQLdb.connect(host="localhost", user=username, passwd=password,
                         db=database, port=3306) as db:
        # Create a cursor using the context manager
        with db.cursor() as cur:
            # Execute the SQL query
            cur.execute("SELECT * FROM states WHERE name LIKE %s", (match,))

            # Fetch all rows and print them
            rows = cur.fetchall()
            for row in rows:
                print(row)