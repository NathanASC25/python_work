
from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


def build_tree(values):
  if not values:
      return None


# Problem 1: Merging Cookie Orders
# You run a local bakery and are given the roots of two binary trees order1 and order2 where each node in the binary tree represents the number of a certain cookie type
#  the customer has ordered. To maximize efficiency, you want to bake enough of each type of cookie for both orders together.

# Given order1 and order2, merge the order together into one tree and return the root of the merged tree. To merge the orders, imagine that when place one tree on top of the other, 
# some nodes of the two trees are overlapped while others are not. If two nodes overlap, then sum node values up as the new value of the merged node. 
# Otherwise, the not None node will be used as the node of the new tree.

# Start the merging process from the root of both orders.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. 
# Assume the input tree is balanced when calculating time complexity.

# class TreeNode():
#      def __init__(self, quantity, left=None, right=None):
#         self.val = quantity
#         self.left = left
#         self.right = right

# def merge_orders(order1, order2):
#     pass
# Example Usage:

# Example 'order1' and 'order2' trees and their merged result


#      1             2         
#     /  \         /   \       
#    3    2       1     3   
#  /               \      \   
# 5                 4      7   

# # Using build_tree() function included at top of page
# cookies1 = [1, 3, 2, 5]
# cookies2 = [2, 1, 3, None, 4, None, 7]
# order1 = build_tree(cookies1)
# order2 = build_tree(cookies2)

# # Using print_tree() function included at top of page
# print_tree(merge_orders(order1, order2))
# Example Usage:

# [3, 4, 5, 5, 4, None, 7]
# Explanation:
# Merged Tree:
#      3
#     /  \      
#   4     5  
#  / \      \
# 5   4      7

# Understand :
# Compare 2 BST , if the curr node is empty or order1.val != order2.val
#     empty node : append the node 
#     order1.val != order2.val : sum of  order1.val + order2.val
#     order1.val == order2.val : append order1.val 


# Plan:
# initialize a emptty BST
#     go through the entire BST , compare order1.val and order2.val
#      empty node : append the node 
#     order1.val != order2.val : sum of  order1.val + order2.val
#         order1.val == order2.val : append order1.val 
#         return the merged BST
    
class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

# Inorder

# Given a binary search tree, inorder will traverse the nodes in sorted ascending order.

# Inorder traversals are commonly used for binary search tree tasks or converting a binary search tree to a sorted list.

def merge_orders(order1, order2):
    order3= []
    curr1=order1
    curr2=order2

    #while curr1 is not None or curr2 is not None:
    if not order1:
            return order2
            
    if not order2:
        return order1
    
    merged = TreeNode(order1.val + order2.val)
    merged.left = merge_orders(order1.left, order2.left)
    merged.right = merge_orders(order1.right, order2.right)

    return merged 
#         elif order1.val != order2.val:
#             sum = order1.val + order2.val
#             return sum
#         elif order1.val == order2.val:
#            return order1

    # order3= merge(order1.left , order2.left) +[ merge(order1.val , order2.val)] + merge(order2.right , order2.right)
    # print (order3)


    #return merge_orders(order1.left , order2.left) +[ merge_orders(order1.val , order2.val)] + merge_orders(order2.right , order2.right)
        
# def inorder(root):
#     if root is None:
#         return []
#     return inorder(root.left) + [root.val] + inorder(root.right)
# # Using build_tree() function included at top of page
# cookies1 = [1, 3, 2, 5]
# cookies2 = [2, 1, 3, None, 4, None, 7]
# order1 = build_tree(cookies1)
# order2 = build_tree(cookies2)

# # Using print_tree() function included at top of page
# print_tree(merge_orders(order1, order2))


# Problem 2
# You are designing a delicious croquembouche (a French dessert composed of a cone-shaped tower of cream puffs 😋), for a couple's wedding.
#  They want the cream puffs to have a variety of flavors. You've finished your design and want to send it to the couple for review.

# Given a root of a binary tree design where each node in the tree represents a cream puff in the croquembouche, that prints a list of the flavors (vals) of each cream puff in level order (i.e., 
# from left to right, level by level).

# Note: The build_tree() and print_tree() functions both use variations of a level order traversal. To get the most out of this problem, we recommend that you reference these 
# functions as little as possible while implementing your solution.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
# Assume the input tree is balanced when calculating time complexity.

# Understand:
# Input: root of the binary tree design
#Output: list of the flavors of each cream puff in level order
# Edge cases: if the not in the root return empty list 

#Plan:
# if design is none return empty list
# initialize a queue with design 
# while loop of queue that is not empty, dequeue the first node and append the node's value to the list
# if node is left, append node to left and if node is right, append node to right
class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    if not design:
        return []

    result = []
    queue = deque([design])
    print(queue)

    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result 
# Example Usage:

# """
#             Vanilla
#            /       \
#       Chocolate   Strawberry
#       /     \
#   Vanilla   Matcha  
# """
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print_design(croquembouche)
# Example Output:

# ['Vanilla', 'Chocolate', 'Strawberry', 'Vanilla', 'Matcha']
