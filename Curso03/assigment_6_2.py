import urllib.request, urllib.parse, urllib.error
import json

APIURL = "http://py4e-data.dr-chuck.net/json?"
APIKEY = 42
params = {}

location = input("Enter location: ")

params = {
    "address" : location,
    "key" : APIKEY
}

finalUrl = APIURL + urllib.parse.urlencode(params)
print("Retrieving ", finalUrl)
urlHandler = urllib.request.urlopen(finalUrl)
data = urlHandler.read().decode()
print("Retrieved", len(data), "characters")

try :
    jsonObject = json.loads(data)
except: 
    jsonObject = None

if not jsonObject :
    print("==== Failure To Retrieve ====")
    # print(data)
    exit()

# print(json.dumps(jsonObject["results"][0], indent = 4))
print("Place id", jsonObject["results"][0]["place_id"])

