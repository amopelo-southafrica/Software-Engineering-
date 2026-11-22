import sqlite3
import unittest
####-------------------------------------------Program description-------------------------------------------------####
print(""" \
BOOKSTORE MANAGEMENT SYSTEM\n

Purpose:\n
Manage bookstore inventory records.\n\n

This program allows authorized users to:\n
- Add new book records\n
- Modify existing book information\n
- Remove books from the system\n
- Search for books by specific criteria\n
- Display all stored book records\n\n

All operations are performed through a menu-driven interface.""")
####-------------------------------------------Program menu-------------------------------------------------####
print("-" * 50)
print("BOOKSTORE MANAGEMENT SYSTEM")
print("-" * 50)
print("Select an operation:")

print("1. Enter book")
print("2. Update book")
print("3. Delete book")
print("4. Search books")
print("5. View all books")
print("0. Exit")
db = sqlite3.connect("ebookstore.db")
cursor = db.cursor()
print(cursor.fetchall())
menu = int(input("Option (0-5): "))
####-------------------------------------------Books table-------------------------------------------------####

#------Create table-----#
cursor.execute(
'''
CREATE TABLE IF NOT EXISTS book (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    authorID INTEGER,
    qty INTEGER
);
'''
)
db.commit()
#------Insert rows-----# 
books=[
    (3001 ,'A Tale of Two Cities ',1290,30),
    (3002 ,'Harry Potter and the Philosophers Stone ',8937,40),
    (3003 ,'The Lion, the Witch and the Wardrobe ',2356,25),
    (3004 ,'The Lord of the Rings ',6380,37),
    (3005 ,'Alices Adventures in Wonderland ',5620,12)]

cursor.execute("SELECT COUNT(*) FROM book")
if cursor.fetchone()[0] == 0:
    cursor.executemany(''' 
        INSERT INTO book (id,title,authorID,qty) 
        VALUES (?,?,?,?) 
    ''', books)
    db.commit() 

####-------------------------------------------Author table-------------------------------------------------####

#------Create table-----# 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS author(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        country TEXT
    )
''')
#------Insert rows-----# 
authors = [
    (1290, 'Charles Dickens', 'England'),
    (8937, 'J.K. Rowling', 'England'),
    (2356, 'C.S. Lewis', 'Ireland'),
    (6380, 'J.R.R. Tolkien', 'South Africa'),
    (5620, 'Lewis Carroll', 'England')]

cursor.execute("SELECT COUNT(*) FROM author")
if cursor.fetchone()[0] == 0:
    cursor.executemany('''
        INSERT INTO author(id,name,country) 
        VALUES (?, ?,?) 
    ''', authors)
    db.commit()
####-------------------------------------------Enter book-------------------------------------------------####

if menu == 1:
    book_title = input("Enter the book title (case-sensitive):")
    book_qty = int(input("Enter the number of copies available:"))
    
    cursor.execute('''
    INSERT INTO book (title, qty)
    VALUES (?, ?)
''', (book_title, book_qty))
    db.commit()
    print("Adding new book to inventory...")

    
####-------------------------------------------Update book-------------------------------------------------####

elif menu == 2:

    #--------------------Submenu--------------------------# 

    option = input(
    "\nWhat would you like to update?\n"
    "a) Book details\n"
    "b) Author ID\n"
    "c) Author information\n"
    "Select an option (a/b/c): "
    )
    #--------------------Submenu: Book-------------------------# 
    if option == "a":
        search_book = input("Enter the current title of the book: ")

    # Check if book exists
        cursor.execute('''
                SELECT title, qty FROM book
                WHERE title = ?
            ''', (search_book,))

        result = cursor.fetchone()

        if result is None:
            print("Book not found.")
        else:
            print(f"Current Title: {result[0]}")
            print(f"Current Quantity: {result[1]}")

        new_title = input("Enter new title (press Enter to keep current): ")
        new_quantity = input("Enter new quantity (press Enter to keep current): ")

        
        if new_title == "":
            new_title = result[0]

        if new_quantity == "":
            new_quantity = result[1]
        else:
            new_quantity = int(new_quantity)

        cursor.execute('''
            UPDATE book
            SET title = ?, qty = ?
            WHERE title = ?
        ''', (new_title, new_quantity, search_book))

        db.commit()
        print("Book updated successfully.")
    #--------------------Submenu: BookID-------------------------# 
    elif option == "c":
        cursor.execute('''
        SELECT
            title,
            qty,
            name,
            country
        FROM book
        INNER JOIN author
        ON book.id = author.author_id''')
        cursor.execute('''
        SELECT
            name,
            country
        FROM author''')
        for row in cursor:
            print("------"*10)
            print(f'Author:{row[0]}\t Country: {row[1]}')
            print("------"*10)
        #--------------------Submenu2-------------------------# 
        submenu = input(
    "\nWhat would you like to change?\n"
    "a) Author name\n"
    "b) Author country\n"
    "Select an option (a/b): "
    )
        #--------------------Submenu2:Authors name-------------------------# 
        if submenu == "a":
            change_authorname = input("Enter the current author name: ")
            new_authorname = input("Enter the new author name:")
            cursor.execute('''
        UPDATE book
        SET author = ?
        WHERE author = ?
        ''', (new_authorname,change_authorname))
        #--------------------Submenu2:Country of author-------------------------# 
        elif submenu == "b":
            change_country = input("Enter the current country name:")
            new_country = input("Enter the new country name:")
            cursor.execute('''
        UPDATE book
        SET author = ?
        WHERE author = ?
        ''', (new_country ,change_country))
####-------------------------------------------Delete  book-------------------------------------------------#### 
elif menu == 3:
    deleted_book = input("Enter the title of the book you want " \
    "to DELETE (this cannot be undone): ")
    cursor.execute('''
    DELETE FROM book
    WHERE title = ?
    ''', (deleted_book,))
    print(" Deleting book from system...")
    
####-------------------------------------------Search books-------------------------------------------------####

elif menu == 4:
    searched = input("Enter the book title you want to search for: ")
    cursor.execute('''
    SELECT title
    FROM book
    WHERE title = ?
    ''', (searched,))
    
####-------------------------------------------View all-------------------------------------------------####

elif menu == 5:
    cursor.execute('''
    SELECT book.title, author.name, author.country, book.qty
    FROM book
    JOIN author ON book.authorID = author.id
    ORDER BY author.name, book.title
    ''')

    rows = cursor.fetchall()

    for row in rows:
        print("-----"*10)
        print(f"Title: {row[0]}")
        print(f"Author: {row[1]}")
        print(f"Country: {row[2]}")
        print(f"Quantity: {row[3]}")
        print("-----"*10)
####-------------------------------------------End-------------------------------------------------####
elif menu == 0:
    print("System exited successfully. Goodbye.")
        
    
