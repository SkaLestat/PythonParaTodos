x = (1, 9, 2) #Tuplas tienen parentesis
print(x)
print(max(x))

(a, b) = (4, "fred")
print(a)
print(b)

d = {
    "b" : 1,
    "a" : 10,
    "c" : 22
}
print(d)
t = sorted(d.items())
print(t)

for e, f in sorted(d.items()) :
    print(e, f)

g = {
    "a" : 10,
    "b" : 1,
    "c" : 22
}
tmp = list()
for k, v in g.items() :
    tmp.append((v, k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

h = {"a" : 10, "b" : 1, "c" : 22}
print(sorted([(v, k) for k, v in h.items()])) #List Comprehension
print(
    sorted(
        [
            (v, k) for k, v in h.items()
        ]
    )
)

x , y = 3, 4
print(y)