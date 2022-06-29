def recursion(n):
    print(n)
    if n == 1:
        return 1
    else:
        return 1+recursion(n/2)


print(recursion(10))
#!===========backtrack permutations
"""# Python function to print permutations of a given list
def permutation(lst):

    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    #!3
    # m= 3
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        # print(str(i) + str(remLst))
        print("=========")
        for p in permutation(remLst):
            print(p)
            l.append([m] + p)
        # print("=========")

    return l


# Driver program to test above function
data = list('abc')
# print(data)
print(permutation(data))
# for p in permutation(data):
#     print(p)
"""
#!==============================
#! ['a', 'b', 'c']
# ['a', 'c', 'b']
# ['b', 'a', 'c']
# ['b', 'c', 'a']
# ['c', 'a', 'b']
# * ['c', 'b', 'a']
# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data
# # Insert Node

#     def insert(self, data):
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#             else:
#                 self.data = data
# # Print the Tree

#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print(self.data),
#         if self.right:
#             self.right.PrintTree()
# # Preorder traversal
# # Root -> Left ->Right

#     def PreorderTraversal(self, root):
#         res = []
#         if root:
#             print("Data"+str(root.data))
#             res.append(root.data)
#             # print("Call self"+str(self.PreorderTraversal(root.left)))
#             res = res + self.PreorderTraversal(root.left)
#             print("RES"+str(res))
#             res = res + self.PreorderTraversal(root.right)
#         return res


# root = Node(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)
# print(root.PreorderTraversal(root))


# #!Post-order Traversal
