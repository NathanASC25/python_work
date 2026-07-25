def sum_of_digits(num):
    total_value = 0
    copy_num = str(num)
    for digit in copy_num:
        num = int(digit)
        total_value += num
    """total_value = 0
    divisor = 1
    copy_num = num
    while (copy_num > 0):
        divisor *= 10
        print(divisor)
    """
    return total_value
# Test Cases
num = 423
print(sum_of_digits(num))

num = 4
print(sum_of_digits(num))
