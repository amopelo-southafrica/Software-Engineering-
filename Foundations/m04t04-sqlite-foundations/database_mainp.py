import sqlite3
db = sqlite3.connect("python_programming.db")
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS python_programming(
        id INTERGER PRIMARY KEY,
        name TEXT,
        grade INTERGER
    )
''')
student_marks =[
    (55,'Carl Davis',61),
    (66,'Dennis Fredrickson',688),
    (77,'Jane Richards',78),
    (12,'Peyton Sawyer',45),
    (2,'Lucas Brooke',99) ]

#Row 1
cursor.executemany(''' 
    INSERT INTO python_programming (id,name, grade) 
    VALUES (?, ?,?) 
''', (student_marks)) 

cursor.execute('''SELECT grade BETWEEN 60 and 80  FROM python_programming''',)

grade = 65
id_change = 55
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id = ?''', (grade, 
id_change)) 

delete_name = "Dennis Fredrickson"
cursor.execute('''DELETE FROM python_programming WHERE name= ?''', (delete_name,)) 

grade = 80
greater = 55
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id > ?''', (grade, 
greater))