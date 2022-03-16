# Tree Leaf Node
# Degree of node is no of children
# Height 0 -         O
# 1 -          O          O

# BT,BST,AVl Tree
#! Used in  Routers, Databases, and  Compilers to build syntax

# from numpy import nonzero


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
print(root.left.value)
