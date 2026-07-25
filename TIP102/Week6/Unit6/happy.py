def happy_number(number):
    container = set()
    while number > 1:
        if number in container:
            return False
        
        container.add(number)
        
        sum = 0
        for digit in str(number):
            num = int(digit)
            sum += pow(num, 2)
        number = sum
        
        '''
        if number in container:
            return False
        sum = 0
        copy = number
        multiplier = 10
        while multiplier * 10 <= copy:
            multiplier *= 10
        while copy > 0:
            result = copy / multiplier
            sum += pow(result, 2)
            multiplier /= 10
            copy /= 10
        container.add(sum)
       ''' 
    
    return True
    

print(happy_number(19))
print(happy_number(2))
