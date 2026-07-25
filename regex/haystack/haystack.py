import re
file = open("actual_data.txt")
nums = 0
for line in file:
    validNums = re.findall("[0-9]+", line)
    for num in validNums:
        nums += int(num)
print(nums)
