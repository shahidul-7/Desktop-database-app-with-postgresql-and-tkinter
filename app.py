import psycopg2
from tkinter import *

# Create tkinter window
window = Tk()


# Establish a connection to the PostgreSQL database
connection = psycopg2.connect(
     dbname="storedb",
     user="postgres",
     password="asdf",
     host="localhost",
     port="5432")

# Create a cursor object to interact with the database
cur_sor = connection.cursor()

# SQL command to create a table
cur_sor.execute("CREATE TABLE IF NOT EXISTS store1 (item TEXT, quantity INTEGER, price REAL)")

# Commit changes to the database
connection.commit()


# #Insert items directly
# def insert_items():
#      cur_sor.execute("INSERT INTO store1 VALUES('Jam', 22, 235)")
#      connection.commit()
# insert_items()

# Insert items dinamically
def insert_items(item, quantity, price):
     cur_sor.execute("INSERT INTO store1 VALUES(%s, %s, %s)", (item, quantity, price))
     connection.commit()

# Update itesm
def update_item(item, quantity, price):
     cur_sor.execute(
          """
          UPDATE store1
          SET price = %s, quantity = %s
          WHERE item = %s
          """, (price, quantity, item)
     )
     connection.commit()

# Delete Items
def delete_item(item):
     cur_sor.execute(
          """
          DELETE FROM store1 
          WHERE item = %s
          """, (item,)
     )
     connection.commit()

# Viw the store items in terminal!
def fetch_items():
     cur_sor.execute("SELECT * FROM store1")
     rows = cur_sor.fetchall()
     for row in rows:
          rows_items = f"Item Name: {row[0]}, Quantity: {row[1]}, Price: {row[2]}"
          if rows_items not in rows:
               print(rows_items)



# insert_items("Lichi", 65, 155)
# update_item("Mango", 45, 45444)
# delete_item("Lichi")
fetch_items()
cur_sor.close()
connection.close()


window.mainloop()