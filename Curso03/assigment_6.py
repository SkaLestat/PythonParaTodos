import urllib.request, urllib.parse, urllib.error
import json

jsonUrl = input("Enter location: ")
print("Retrieving ", jsonUrl)
urlHandler = urllib.request.urlopen(jsonUrl)
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

print("count:", len(jsonObject["comments"]))

countValues = []
for comment in jsonObject["comments"] :
    countValues.append(int(comment["count"]))
print("Sum", sum(countValues))
