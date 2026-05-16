name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hourInstancesCount = dict()
for line in handle:
    if "From" in line:
        line = line.split()
        for word in line:
            if ":" in word and len(word) == 8:
                time = word.split(":")
                hourInstancesCount[time[0]] = hourInstancesCount.get(time[0], 0) + 1
                break
pairs = list()
for key, value in hourInstancesCount.items():
    pairs.append((key, value))
pairs = sorted(pairs)
for pair in pairs:
    print(pair[0], pair[1])
