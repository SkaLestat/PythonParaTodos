name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hours = dict()

for lines in handle :
    if "From " in lines :
        currentSender = lines.split()
        hour = currentSender[5].split(":")
        hours[hour[0]] = hours.get(hour[0], 0) + 1

sortedHours = sorted([(k, v) for k, v in hours.items()])
for k, v in sortedHours : 
    print(k, v)
