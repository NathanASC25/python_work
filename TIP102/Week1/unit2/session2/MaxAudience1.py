def max_audience_performances(audiences):
    max_value = 0
    total = 0
    lastIndexesVisited = list()
    # Bug - keeps track of indexes despite not being highest value
    for i in range(len(audiences)):
        if audiences[i] > max_value:
            max_value = audiences[i]
            lastIndexesVisited.append(i)
    total += max_value
    for i in range(len(audiences)):
        if audiences[i] == max_value and i not in lastIndexesVisited:
            total += audiences[i]
    return total
# Test Cases
audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
