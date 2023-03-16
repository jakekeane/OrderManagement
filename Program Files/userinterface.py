import os
create_path = os.path.abspath("createorder.py")
read_path = os.path.abspath("readorders.py")
delete_path = os.path.abspath("deleteorder.py")
database_path = os.path.abspath("createdb.py")

print("QACafe Order Management System\n")
selectOption = int(input("""Please select an option:\n
1. Create/Initiate the Database (RUN ONCE)
2. Create an order 
3. Read an order
4. Update an order
5. Delete an order
6. Delete ALL orders\n\n"""))

if selectOption == 1:
  exec(open(database_path).read())
elif selectOption == 2:
  exec(open(create_path).read())
elif selectOption == 3:
  exec(open(read_path).read())
elif selectOption == 5:
  exec(open(delete_path).read())
