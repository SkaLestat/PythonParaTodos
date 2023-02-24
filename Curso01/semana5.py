x = 10
if x < 10 :
    print("Smaller")
if x > 10 : print("Bigger than 10")
if x > 20 :
    print("Bigger")
else :
    print("between 10 and 20")
print("Finish")

########################

a = 5
if a < 2 :
    print("small")
elif a < 10 :
    print("medium")
else :
    print("large")
print("All Done")


astr = "Hello Bob"
try :
    istr = int(astr)
except :
    istr = -1
print("First", istr)
