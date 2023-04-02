fname = input("Enter file name: ")
# fname = "romeo.txt"
fh = open(fname)
lst = list()
currentString = None
for line in fh:
    # print(line.rstrip())
    currentString = line.rstrip().split()
    for string in currentString :
        if string in lst : continue
        lst.append(string)
lst.sort()
print(lst)