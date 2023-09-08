import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

apiKey = False

if apiKey is False :
    serviceUrl = "http://py4e-data.dr-chuck.net/geojson?"
else :
    serviceUrl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

connection = sqlite3.connect("geodata.sqlite")
cursor = connection.cursor()

cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS Locations(
        address TEXT,
        geodata TEXT
    );
""")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fileHandler = open("where.data")
count = 0
for line in fileHandler:
    if count > 200 :
        print("Retrieved 200 locations, restart to retrieve more")
        break

    address = line.strip()
    print("")
    cursor.execute("""
        SELECT geodata FROM Locations WHERE address = ?
    """, (memoryview(address.encode()), ))

    try :
        data = cursor.fetchone()[0]
        print("Found in database ", address)
        continue
    except :
        pass #se usa para evitar error por dejar vacio donde deberia existir codigo

    params = dict()
    params["query"] = address

    if apiKey is not False :
        params["key"] = apiKey
    url = serviceUrl + urllib.parse.urlencode(params)

    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context = ctx)
    data = uh.read().decode()
    print("Retrieved", len(data), "Characters", data[:20].replace("\n", ""))
    coutn = count + 1

    try: 
        js = json.loads(data)
    except :
        print(data) #print in case unicode cause an error
        continue
    if "status" not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print("==== Failure to Retrieve ====")
        print(data)
        break

    cursor.execute("""
        INSERT INTO Locations (address, geodata)
        VALUES (?, ?)
    """, (memoryview(address.encode()), memoryview(data.encode())))
    connection.commit()
    if count % 10 == 0 :
        print("Pausing for a bit...")
        time.sleep(0.5)

print("Run semana5_2.py to read the data from the database so you can vizualize it on a map.")

