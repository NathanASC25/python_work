
'''
Given the root of a binary tree where each node represents the number of splits in a leaf of a Monstera plant, return the number of Monstera leaves 🍃 

that have an odd number of splits.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

Note: The term leaf in this problem refers to the plant leaf 🍃 of a Monstera plant, not the type of node leaf nodes which are nodes with no children.
'''
from collections import deque
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def count_odd_splits(root):
    def inorder_traverse(root):
        if not root:
            return 0
        '''
        inorder_traverse(root.left)
        if root.val %2 != 0:
            count += 1
        inorder_traverse(root.right)
        '''
        if root.val % 2 != 0:
            return 1 + inorder_traverse(root.left) + inorder_traverse(root.right)
        else:
            return inorder_traverse(root.left) + inorder_traverse(root.right)

    return inorder_traverse(root) 
    
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

            
        
    pass

"""
      2
     / \
    /   \
   3     5
  / \     \
 6   7     12
"""

# Using build_tree() function included at top of page
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))
