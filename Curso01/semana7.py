#LoopsAndIteration
while True :
    line = input("> ")
    if line == "done" :
        break #out of the loop
    print(line)
print("Done!")

while True :
    line2 = input("> ")
    if line2[0] == "#" : #Access character at line 0
        continue #go to the next iteration
    if line2 == "done" :
        break #out of the loop
    print(line2)
print("Done!")