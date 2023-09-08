import sqlite3

connection = sqlite3.connect("assigment_1.sqlite") #Create file if not exists
cursor = connection.cursor()

cursor.execute("""DROP TABLE IF EXISTS Counts""")
cursor.execute("""CREATE TABLE Counts (org TEXT, count INTEGER)""")

fileName = input("Enter file name: ")
if(len(fileName) < 1) :
    fileName = "mbox.txt"
fileHandler = open(fileName)
for line in fileHandler :
    if not line.startswith("From: ") :
        continue
    pieces = line.split()
    mail = pieces[1].split("@")
    org = mail[1]
    cursor.execute("SELECT count FROM Counts WHERE org = ? ", (org,))
    row = cursor.fetchone()
    if row is None :
        cursor.execute("""INSERT INTO Counts (org, count)
        VALUES (?, 1)""", (org,))
    else :
        cursor.execute("""UPDATE Counts SET count = count + 1 WHERE org = ?""", (org,))

connection.commit()

sqlString = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10"

for row in cursor.execute(sqlString):
    print(str(row[0]), row[1])

cursor.close()