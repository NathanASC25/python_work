def is_valid_post_format(posts):
    stack = []
    valid_opened = ("(", "[", "{")
    valid_closed = (")", "]", "}")
    for elem in posts:
        if elem in valid_opened:
            stack.append(elem)
        if elem in valid_closed:
            if stack[len(stack) - 1] == "(" and elem != ")":
                return False
            if stack[len(stack) - 1] == "[" and elem != "]":
                return False
            if stack[len(stack) - 1] == "{" and elem != "}":
                return False
            stack.pop()
    return True
# Test Cases
print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
