import json as JSON
import sqlite3 as SQ

connection = SQ.connect("rosterdb.sqlite")
cursor = connection.cursor() #File handler for DB

# Make some fresh tables using executescript #
cursor.executescript(""" 
    DROP TABLE if EXISTS User;
    DROP TABLE if EXISTS Member;
    DROP TABLE if EXISTS Course;
                     
    CREATE TABLE User(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
    
    CREATE TABLE Course(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE
    );
    
    CREATE TABLE Member(
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
	    PRIMARY KEY (user_id, course_id)             
    );
 """)

fileName = input("Enter file name: ")
if(len(fileName) < 1):
    fileName = "roster_data_sample.json"


stringData = open(fileName).read()
jsonData = JSON.loads(stringData)

for entry in jsonData:
    
    name = entry[0]
    title = entry[1]
    print(name, title)
    print((name, title))#print as tuple
    

    cursor.execute("""
        INSERT OR IGNORE INTO User(name)
        VALUES (?)
    """, (name,))
    cursor.execute("""
        SELECT id FROM User WHERE name = ?
    """, (name,))
    user_id = cursor.fetchone()[0]

    cursor.execute("""
        INSERT OR IGNORE INTO Course(title)
        VALUES (?)
    """, (title,))
    cursor.execute("""
        SELECT id FROM Course WHERE title = ?
    """, (title,))
    course_id = cursor.fetchone()[0]

    cursor.execute("""
        INSERT OR REPLACE INTO Member(user_id, course_id)
        VALUES (?, ?)
    """, (user_id, course_id))
    connection.commit()