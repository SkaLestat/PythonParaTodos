# Use words.txt as the file name
fileName = input("Enter the file name: ")
try :
    theFile = open(fileName)
except :
    print("File cannot be opened:", fileName)
    quit()
theData = theFile.read()
print(theData.upper().rstrip())