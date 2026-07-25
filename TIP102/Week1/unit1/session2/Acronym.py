def is_acronym(words, s):
    first_letters = ""
    for word in words:
        first_letters += word[0]
    return first_letters == s
# Test Cases
words = ["christopher", "robin", "milne"]
s = "crm"
print(is_acronym(words, s))
