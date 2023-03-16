import sqlite3 as s

con = s.connect('orders.db')
c = con.cursor()

c.execute("""
    CREATE TABLE ORDERS (
        order_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT,
        drink TEXT,
        size TEXT,
        extras TEXT,
        price REAL(2)
    );
""")

con.commit()
con.close()
