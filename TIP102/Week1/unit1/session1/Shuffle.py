def shuffle(cards):
    y_values = list()
    index = int(len(cards) / 2)
    while index < len(cards):
        y_values.append(cards[index])
        index += 1
    index = 1
    y_val_index = 0
    while index < int(len(cards) / 2):
        temp = cards[index]
        cards[index] = y_values[y_val_index]
        cards[index - 1 + int(len(cards) / 2)] = temp
        y_val_index += 1
        index += 2
    print(index)
    return cards
# Test cases
cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
print(shuffle(cards))

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
print(shuffle(cards))

cards = [10, 10, 2, 2]
print(shuffle(cards))
