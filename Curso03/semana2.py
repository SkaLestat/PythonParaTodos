import re

x = "My 2 favorite numbers are 19 and 42"
y = re.findall("[0-9]+", x)
print(y)
y = re.findall("[AEIOU]+", x)
print(y)

#Greedy Matching => Match largest possible string
x = "From: Using the : character"
y = re.findall("^F.+:", x)
print(y)
#Non Greedy
x = "From: Using the : character"
y = re.findall("^F.+?:", x)
print(y)

x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall("\S+@\S+", x)
print(y)

x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall("^From (\S+@\S+)", x)
print(y)

x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall("@([^ ]*)", x)
print(y)

x = "We just received $10.00 for cookies"
y = re.findall("\$[0-9.]+", x)
print(y)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)