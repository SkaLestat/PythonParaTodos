import re

name = input("Enter file name:")
if len(name) < 1:
    name = "regex_sum_1742916.txt"
currentText = open(name)
numbers = []

for lines in currentText:
    if(len(re.findall("[0-9]+", lines)) > 0):
        for numInList in re.findall("[0-9]+", lines):
            numbers.append(int(numInList))

print(len(numbers))
print(sum(numbers))
