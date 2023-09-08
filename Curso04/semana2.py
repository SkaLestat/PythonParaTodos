import sqlite3

connection = sqlite3.connect("emaildb.sqlite") #Create file if not exists
cursor = connection.cursor()

cursor.execute("""DROP TABLE IF EXISTS Counts""")
cursor.execute("""CREATE TABLE Counts (email TEXT, count INTEGER)""")

fileName = input("Enter file name: ")
if(len(fileName) < 1) :
    fileName = "mbox-short.txt"
fileHandler = open(fileName)
for line in fileHandler :
    if not line.startswith("From: ") :
        continue
    pieces = line.split()
    email = pieces[1]
    cursor.execute("SELECT count FROM Counts WHERE email = ? ", (email,)) #Trailing comma, ? => Placeholder
    row = cursor.fetchone()
    if row is None :
        cursor.execute("""INSERT INTO Counts (email, count)
        VALUES (?, 1)""", (email,))
    else :
        cursor.execute("""UPDATE Counts SET count = count + 1 WHERE email = ?""", (email,)) #En este caso se coloca la coma en la Tupla por que solo tiene un valor
    connection.commit() #puede ser lento, guarda el estado de la db?

# https://sqlite.org/lang_select.html
sqlString = "SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10"

for row in cursor.execute(sqlString):
    print(str(row[0]), row[1]) #sobra el "str" ???

cursor.close()
