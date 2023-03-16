import sqlite3 as s

con = s.connect('orders.db')
cur = con.cursor()

customer_name=input("What was the customer's name? ")
drink = input("What item was purchased? ")
size = input("What size was the drink? ")
extras = input("What were the extras? ")
price = float(input("What was the price of the drink? "))

sql = 'INSERT INTO ORDERS (customer_name, drink, size, extras, price) values(?, ?, ?, ?, ?)'
data = (customer_name, drink, size, extras, price)

cur.execute(sql, data)

con.commit()
con.close()