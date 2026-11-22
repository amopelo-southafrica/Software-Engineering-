import sqlite3
import unittest
####-------------------------------------------Books table-------------------------------------------------####

#------Create table-----#
def setup_database():
    db = sqlite3.connect("ebookstore.db")
    cursor = db.cursor()
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
    db.close()

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
    return db, cursor
####-------------------------------------------Enter book-------------------------------------------------####
def add_book(cursor, db):
    book_title = input("Enter the book title: ")
    author_id = int(input("Enter the author ID: "))
    book_qty = int(input("Enter the number of copies available: "))

    cursor.execute("""
    INSERT INTO book (title, authorID, qty)
    VALUES (?, ?, ?)
    """, (book_title, author_id, book_qty))

    db.commit()

    print("Book added successfully.")

    
####-------------------------------------------Update book-------------------------------------------------####

def update_book(cursor,db):

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
                    book.title,
                    book.qty,
                    author.name,
                    author.country
                FROM book
                INNER JOIN author
                ON book.authorID = author.authorID
                ''')

        for row in cursor:
            print("------"*10)
            print(f'Title: {row[0]}')
            print(f'Quantity: {row[1]}')
            print(f'Author: {row[2]}')
            print(f'Country: {row[3]}')
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

            change_authorname = input("Enter current author name: ")
            new_authorname = input("Enter new author name: ")

            cursor.execute("""
            UPDATE author
            SET name = ?
            WHERE name = ?
            """, (new_authorname, change_authorname))

            db.commit()

            #--------------------Submenu2:Country of author-------------------------# 
        elif submenu == "b":

            change_country = input("Enter current country: ")
            new_country = input("Enter new country: ")

            cursor.execute("""
                UPDATE author
                SET country = ?
                WHERE country = ?
            """, (new_country, change_country))
####-------------------------------------------Delete  book-------------------------------------------------#### 
def delete_book(cursor):
    deleted_book = input("Enter the title of the book you want " \
    "to DELETE (this cannot be undone): ")
    cursor.execute('''
    DELETE FROM book
    WHERE title = ?
    ''', (deleted_book,))
    print(" Deleting book from system...")
    
####-------------------------------------------Search books-------------------------------------------------####

def search_books(cursor):
    searched = input("Enter the book title you want to search for: ")

    cursor.execute('''
        SELECT id, title, authorID, qty
        FROM book
        WHERE title = ?
    ''', (searched,))

    result = cursor.fetchone()

    if result:
        print("------"*10)
        print(f"ID: {result[0]}")
        print(f"Title: {result[1]}")
        print(f"Author ID: {result[2]}")
        print(f"Quantity: {result[3]}")
        print("------"*10)
    else:
        print("Book not found.")
    
####-------------------------------------------View all-------------------------------------------------####

def view_books(cursor):
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

def exit():
    print("System exited successfully. Goodbye.")
####-------------------------------------------End-------------------------------------------------####

####-------------------------------------------Program menu-------------------------------------------------####        
def main_menu(cursor, db):

    while True:
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

        menu = int(input("Option (0-5): "))

        if menu == 1:
            add_book(cursor, db)

        elif menu == 2:
            update_book(cursor, db)

        elif menu == 3:
            delete_book(cursor, db)

        elif menu == 4:
            search_books(cursor)

        elif menu == 5:
            view_books(cursor)

        elif menu == 0:
            print("Goodbye.")
            break

        else:
            print("Invalid option.")
db, cursor = setup_database()
main_menu(cursor, db)
