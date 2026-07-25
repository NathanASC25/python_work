from collections import deque
'''
You are looking to buy a new flower plant for your garden. The nursery you visit stores its inventory in a binary search tree (BST) where each node represents a plant
in the store. The plants are organized according to their names (vals) in alphabetical order in the BST.

Given the root of the binary search tree inventory and a target flower name, write a function find_flower() that returns True if the flower is present in the garden 
and False otherwise.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. 
Assume the input tree is balanced when calculating time complexity.
'''

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def find_flower(inventory, name):
    if inventory is None:
        return False
    if inventory.val == name:
        return True
    return find_flower(inventory.left, name)
    return find_flower(inventory.right, name)
    return False
    pass
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i<len(values):
        current = queue.popleft()
        if i< len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
            i += 1
        if i< len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
            i += 1
    return root
"""
         Rose
        /    \
      Lilac   Tulip
     /  \       \
  Daisy  Lily  Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]

garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 
