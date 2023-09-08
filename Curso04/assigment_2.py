import xml.etree.ElementTree as ET
import sqlite3 as SQ

connection = SQ.connect("assigment_2.sqlite")
cursor = connection.cursor()

# Make some fresh tables using executescript #
cursor.executescript(""" 
    DROP TABLE if EXISTS Artist;
    DROP TABLE if EXISTS Album;
    DROP TABLE if EXISTS Genre;
    DROP TABLE if EXISTS Track;
                     
    CREATE TABLE Artist(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
    
    CREATE TABLE Genre(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
                     
    CREATE TABLE Album(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        artist_id INTEGER
    );
    
    CREATE TABLE Track(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        album_id INTEGER,
        genre_id INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    );
 """)

fileName = input("Enter file name: ")
if(len(fileName) < 1):
    fileName = "Library.xml"

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(data, key):
    found = False
    for child in data:
        if found:
            return child.text
        # if(child.tag == "key" and child.text == key):
        if child.tag == "key" and child.text == key:
            found = True
    return None

stuff = ET.parse(fileName)
all = stuff.findall("dict/dict/dict")
print("Dict count:", len(all))

for entry in all:
    if(lookup(entry, "Track ID") is None):
        continue

    name = lookup(entry, "Name")
    artist = lookup(entry, "Artist")
    genre = lookup(entry, "Genre")
    album = lookup(entry, "Album")
    count = lookup(entry, "Play Count")
    rating = lookup(entry, "Rating")
    length = lookup(entry, "Total Time")

    if name is None or artist is None or album is None or genre is None:
        continue
    print(name, artist, album, count, rating, length)

    cursor.execute("""
        INSERT OR IGNORE INTO Artist(name) VALUES (?)
    """, (artist,))
    cursor.execute("""
        SELECT id FROM Artist WHERE name = ?
    """, (artist,))
    artist_id = cursor.fetchone()[0]
    
    cursor.execute("""
        INSERT OR IGNORE INTO Genre(name) VALUES (?)
    """, (genre,))
    cursor.execute("""
        SELECT id FROM Genre WHERE name = ?
    """, (genre,))
    genre_id = cursor.fetchone()[0]

    cursor.execute("""
        INSERT OR IGNORE INTO Album(title, artist_id) VALUES (?, ?)
    """, (album, artist_id))
    cursor.execute("""
        SELECT id FROM Album WHERE title = ?
    """, (album,))
    album_id = cursor.fetchone()[0]

    cursor.execute("""
        INSERT OR REPLACE INTO Track(title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)
    """, (name, album_id, genre_id, length, rating, count))
    connection.commit()