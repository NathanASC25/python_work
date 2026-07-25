def max_audience_performances(audiences):
    max_value = 0
    total = 0
    last_indexes_visited = dict()
    last_index = 0
    for i in range(len(audiences)):
        if audiences[i] > max_value:
            max_value = audiences[i]
            last_index = i
    last_indexes_visited[last_index] = max_value
    total += max_value
    for i in range(len(audiences)):
        if audiences[i] == max_value and i not in last_indexes_visited:
            total += max_value
            last_indexes_visited[i] = audiences[i]
    return total
# Test Cases
audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
