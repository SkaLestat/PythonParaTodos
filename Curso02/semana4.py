abc = "With three words"
stuff = abc.split()
print(stuff)
# print(stuff.sort()) # no sirve de esta forma
stuff.sort()
print(stuff)
print(len(stuff))
print(stuff[0])

for w in stuff:
    print(w)


# fruit = 'Banana'
# fruit[0] = 'b'
# print(fruit)