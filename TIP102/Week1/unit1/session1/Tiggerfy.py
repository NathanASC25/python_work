def tiggerfy(s):
    remove_letters = ["t", "i", "g", "e", "r"]
    newStr = list(s)
    s = ""
    for letter in newStr:
        if letter.lower() not in remove_letters:
            s += letter
            continue
        if "c" in newStr and "c" not in s:
            s += "c"
        newStr.remove(letter)
    return s
# Test Cases
s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))
