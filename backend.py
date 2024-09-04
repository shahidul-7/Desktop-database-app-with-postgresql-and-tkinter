import sqlite3

# Create Table
def connect():
     connecton = sqlite3.connect("bookstore.db")
     cur_sor = connecton.cursor()
     cur_sor.execute("CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
     connecton.commit()
     connecton.close()

# Add Entry
def add_entry(title, author, year, isbn):
     connecton = sqlite3.connect("bookstore.db")
     cur_sor = connecton.cursor()
     cur_sor.execute("INSERT INTO bookstore VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))
     connecton.commit()
     connecton.close()  

# Fatch the store
def fatch_bookstore():
     connecton = sqlite3.connect("bookstore.db")
     cur_sor = connecton.cursor()
     cur_sor.execute("SELECT * FROM bookstore")
     rows = cur_sor.fetchall()
     connecton.close() 
     # for row in rows: 
     #      print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Year: {row[3]}, ISBN: {row[4]}")
     return rows

# Search in the Book store
def search_bookstore(title="", author="", year="", isbn=""):
     connecton = sqlite3.connect("bookstore.db")
     cur_sor = connecton.cursor()
     cur_sor.execute("SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
     rows = cur_sor.fetchall()
     connecton.close() 
     return rows


# Delete an item
def delete_item(id):
     connecton = sqlite3.connect("bookstore.db")
     cur_sor = connecton.cursor()
     cur_sor.execute("DELETE FROM bookstore WHERE id=?", (id,))
     connecton.commit()
     connecton.close() 

# Update an item
def update_item(id, title, author, year, isbn):
     connecton = sqlite3.connect("bookstore.db")
     cur_sor = connecton.cursor()
     cur_sor.execute("UPDATE bookstore SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
     connecton.commit()
     connecton.close() 

connect()


update_item(28, "Boner Bagh", "Tiger", 4566, 343334333)
print(fatch_bookstore())
