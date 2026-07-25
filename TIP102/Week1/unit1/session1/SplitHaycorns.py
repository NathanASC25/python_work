def split_haycorns(quantity):
    num_ways = list()
    copy = quantity
    while (copy >= 1):
        if copy <= 3:
            if quantity % copy == 0:
                num_ways.append(int(copy))
            copy -= 1
            continue
        num_ways.append(int(copy))
        copy /= 2
    num_ways.reverse()
    return num_ways
# Test Cases
quantity = 6
print(split_haycorns(quantity))

quantity = 1
print(split_haycorns(quantity))
