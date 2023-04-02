# Use the file name mbox-short.txt as the file name
fileName = input("Enter the file name: ")
# fileName = "mbox-short.txt"
try :
    theFile = open(fileName)
except :
    print("File cannot be opened:", fileName)
    quit()

average = 0
counter = 0

for line in theFile:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    counter += 1
    indexSpace = line.find(" ")
    average += float(line[indexSpace + 1 : ])
print("Average spam confidence:", average/counter)