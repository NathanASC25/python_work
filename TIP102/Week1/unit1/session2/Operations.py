def final_value_after_operations(operations):
    total_sum = 1
    for operation in operations:
        if operation == "bouncy" or operation == "flouncy":
            total_sum += 1
        if operation == "trouncy" or operation == "pouncy":
            total_sum -= 1
    return total_sum
# Test Cases
operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))
