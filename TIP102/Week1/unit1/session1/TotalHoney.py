def sum_honey(hunny_jars):
    total_honey = 0
    for jar in hunny_jars:
        total_honey += jar
    return total_honey
# Test cases
hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))
