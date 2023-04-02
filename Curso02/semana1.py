fruit = "banana"
print(len(fruit))
letter = fruit[1]
print(letter)

x = 3
w = fruit[x - 1]
print(w)

index = 0
while index < len(fruit) :
    char = fruit[index]
    print(index, char)
    index += 1

for char2 in fruit :
    print(char2)

string1 = "Monty Python"
#index operator
print(string1[0 : 4]) #up to but not include 4
print(string1[6 : 7])
print(string1[6 : 20]) #no da error asi supere la cantidad de caracteres
print(string1[: 7])
print(string1[8 :])
print(string1[:])

print("n" in fruit)
print("m" in fruit)
print("nan" in fruit)

if "a" in fruit :
    print("found it")

#if word < "banana" => Mayusculas son menores que Minusculas A < a, Z < a

greet = "Hello Bob"
zap = greet.lower()
print(zap)
print("Hi There".lower())
print(type(zap))
print(dir(zap))

pos = fruit.find("na")
print(pos)
noPos = fruit.find("zz")
print(noPos)

replaceGreet = greet.replace("Bob", "Jane")
print(replaceGreet)
replaceChar = greet.replace("o", "X")
print(replaceChar)

spacesGreet = "   Hello Bob   "
print(spacesGreet.lstrip())
print(spacesGreet.rstrip())
print(spacesGreet.strip())

line = "Please have a nice day"
print(line.startswith("Please"))
print(line.startswith("p"))

dataString = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
atpos = dataString.find("@")
print(atpos)

sppos = dataString.find(" ", atpos)
print(sppos)

host = dataString[atpos+1 : sppos]
print(host)