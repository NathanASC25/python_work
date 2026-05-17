import re
file = open("nums.txt")
lines = ""
str = "[0-9]+"
for line in file:
    lines += line
arr = re.findall(str, lines)
print("\n", arr ,"\n")
