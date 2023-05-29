import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"
while True :
    address = input("Enter Location: ")
    if(len(address) < 1) : break

    url = serviceurl + urllib.parse.urlencode(
        {
            "address" : address
        }
    )
    print("Retrieving", url)
    urlHandler = urllib.request.urlopen(url)
    data = urlHandler.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        jsonObject = json.loads(data)
    except:
        jsonObject = None
    
    if not jsonObject or "status" not in jsonObject or jsonObject["status"] != "OK" :
        print("==== Failure To Retrieve ====")
        print(data)
        continue

    print(json.dumps(jsonObject, indent = 4))

    lat = jsonObject["results"][0]["geometry"]["location"]["lat"]
    lng = jsonObject["results"][0]["geometry"]["location"]["lng"]
    print("lat", lat, "lng", lng)
    location = jsonObject["results"][0]["formatted_address"]