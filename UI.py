import os
create_path = os.path.abspath("addorder.py")
read_path = os.path.abspath("readorders.py")
delete_path = os.path.abspath("deleteorder.py")

print("QACafe Order Management System\n")
selectOption = int(input("""Please select an option:\n
1. Create an order 
2. Read an order
3. Update an order
4. Delete an order
5. Delete ALL orders\n\n"""))

if selectOption == 1:
  exec(open(create_path).read())
elif selectOption == 2:
  exec(open(read_path).read())
elif selectOption == 4:
  exec(open(delete_path).read())
