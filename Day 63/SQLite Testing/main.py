import sqlite3

# Create a connection to a new database
db = sqlite3.connect("books-collection.db")
# Run main.py, and you will see a new file appear called books-collection.db
# Next we need to create a cursor which will control our database.
"""
So a cursor is also known as the mouse or pointer. If we were working in Excel or Google Sheet, we would be using the 
cursor to add rows of data or edit/delete data, we also need a cursor to modify our SQLite database.
"""
cursor = db.cursor()

"""
Let's break this down.

cursor - We created this in step 4 and this is the mouse pointer in our database that is going to do all the work.

.execute() - This method will tell the cursor to execute an action. All actions in SQLite databases are expressed 
             as SQL (Structured Query Language) commands. These are almost like English sentences with keywords 
             written in ALL-CAPS. There are quite a few SQL commands. But don't worry, you don't have to memorise them.

CREATE TABLE -  This will create a new table in the database. The name of the table comes after this keyword.
                Docs: https://www.w3schools.com/sql/sql_ref_create_table.asp
                
books -  This is the name that we've given the new table we're creating.

() -  The parts that come inside the parenthesis after CREATE TABLE books ( ) are going to be the fields in this table. 
      Or you can imagine it as the Column headings in an Excel sheet.
      
id INTEGER PRIMARY KEY -  This is the first field, it's a field called "id" which is of data type INTEGER and it 
                          will be the PRIMARY KEY for this table. The primary key is the one piece of data that 
                          will uniquely identify this record in the table. e.g. The primary key of humans might be 
                          their passport number because no two people in the same country has the same passport number.
                          
title varchar(250) NOT NULL UNIQUE -  This is the second field, it's called "title" and it accepts 
                                      a variable-length string composed of characters. The 250 in brackets is the 
                                      maximum length of the text. NOT NULL means it must have a value and cannot be 
                                      left empty. UNIQUE means no two records in this table can have the same title.
                                      
author varchar(250) NOT NULL -  A field that accepts variable-length Strings up to 250 characters called author that 
                                cannot be left empty.
                                
rating FLOAT NOT NULL -  A field that accepts FLOAT data type numbers, cannot be empty and the field is called rating.                                                                     
"""
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) "
               "NOT NULL, rating FLOAT NOT NULL)")
