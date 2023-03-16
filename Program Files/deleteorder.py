import sqlite3 as s

con = s.connect('orders.db')
cur = con.cursor()

delete = input("Please enter the Order ID to delete: ")

cur.execute('DELETE FROM orders WHERE order_id=?', (delete,))

con.commit()
con.close()