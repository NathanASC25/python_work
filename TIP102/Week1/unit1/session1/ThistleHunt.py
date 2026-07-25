def locate_thistles(items):
    thistle_indices = list()
    for index in range(len(items)):
        if items[index].lower() == "thistle":
            thistle_indices.append(index)
    return thistle_indices
# Test Cases
items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))
