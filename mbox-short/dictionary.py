name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
senders = dict()
bigCount = 0
bigName = ""
handle = open(name)
for line in handle:
    line = line.split(" ")
    if "From" in line:
        senders[line[1]] = senders.get(line[1], 0) + 1
        count = senders[line[1]]
        if bigCount == None or count > bigCount:
            bigCount = count
            bigName = line[1]
print(bigName, bigCount)
