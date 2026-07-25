def doubled(hunny_jars):
    for i in range(len(hunny_jars)):
        hunny_jars[i] = hunny_jars[i] * 2
    return hunny_jars
# Test cases
hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))
