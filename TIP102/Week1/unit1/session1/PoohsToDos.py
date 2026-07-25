def print_todo_list(tasks):
    print("Pooh's To Dos:")
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]}")
# Test Cases
task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)
