def delete_minimum_elements(hunny_jar_sizes):
    ordered = list()
    iterations = 0
    maximum = hunny_jar_sizes[0]
    indexes_visited = list()
    last_index_visited = 0
    for jar in hunny_jar_sizes:
        if jar > maximum:
            maximum = jar
    minimum = maximum
    while iterations < len(hunny_jar_sizes):
        index = 0
        for jar in hunny_jar_sizes:
            if jar < minimum and index not in indexes_visited:
                minimum = jar
                last_index_visited = index
            index += 1
        indexes_visited.append(last_index_visited)
        ordered.append(minimum)
        minimum = maximum
        iterations += 1
    return ordered
# Test Cases
hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))
