import sqlite3 as s

con = s.connect('orders.db')
cur = con.cursor()

query = input("Please enter your order query: ")

data = cur.execute(query)

for row in data:
    print(row)

con.close()