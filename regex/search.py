import re
file = open("nums.txt")
nums = list()
str = "[0-9]+"
for line in file:
    validNums = re.findall(str, line)
    for num in validNums:
        nums.append(num)
print("\n", nums ,"\n")
