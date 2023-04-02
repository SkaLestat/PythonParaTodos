purse = dict()
purse["money"] = 12
purse["candy"] = 3
purse["tissues"] = 75
print(purse)
print(purse["candy"])
purse["candy"] = purse["candy"] + 2
print(purse)


ccc = dict()
ccc["csev"] = 1
ccc["cwen"] = 1
print(ccc)
ccc["cwen"] += 1
print(ccc)

print("cxev" in ccc)

getFromCcc = ccc.get("cxev", 0)#0 es el default si no encuentra valor
print(getFromCcc)

jjj = {
    "chuck" : 1, 
    "fred" : 43,
    "jan" : 100
}

print(jjj)
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

for word, count in jjj.items() :
    print(word, count)

print(max(jjj))