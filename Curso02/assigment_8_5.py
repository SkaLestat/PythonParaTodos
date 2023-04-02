fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

mailList = list()
fh = open(fname)
count = 0

for mail in fh :
    mail = mail.rstrip().split()
    for string in mail :
        if "From" != string : continue
        mailList.append(mail[1])
        print(mail[1])
count = len(mailList)
print("There were", count, "lines in the file with From as the first word")
