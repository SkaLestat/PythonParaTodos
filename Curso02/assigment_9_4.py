name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

senders = dict()

for lines in handle :
    if "From:" in lines :
        currentSender = lines.split()
        senders[currentSender[1]] = senders.get(currentSender[1], 0) + 1

sender = None
totalSended = None

for mail, total in senders.items() :
    if sender is None or total > totalSended :
        sender = mail
        totalSended = total
print(sender, totalSended)
