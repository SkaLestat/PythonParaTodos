import json

data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)#produce traceback si hay un error de sintaxis en json
print(info)
print("Name:", info["name"])
print("Hide:", info["email"]["hide"])

data2 = '''[
    {
        "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    },
    {
        "id" : "009",
        "x" : "7",
        "name" : "Chucks"
    }
]'''

info2 = json.loads(data2)
print("User count:", len(info2))
for item in info2 :
    print("Name", item["name"])
    print("Id", item["id"])
    print("Attribute", item["x"])