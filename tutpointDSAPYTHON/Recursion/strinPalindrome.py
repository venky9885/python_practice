
class Solution:
    def minOperations(self, nums, x: int, c=0) -> int:
        if(x == 0):
            print(nums)
            return c

        if(nums[0] <= x):
            if(nums[0] >= nums[-1]):
                t = nums.pop(0)
                x = x-t
                c += 1
                return self.minOperations(nums, x, c)
        if(nums[-1] <= x):
            if(nums[-1] >= nums[0]):
                t = nums.pop(-1)
                x = x-t
                c += 1
                return self.minOperations(nums, x, c)
        else:
            return -1


t = Solution()
t.minOperations([3, 2, 20, 1, 1, 3], 10)
# print(dpg([-2, 1, -3, 4, -1, 2, 1, -5, 4], {}, 0))
# class Node:
#     def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None


# class SLinkedList:
#     def __init__(self):
#         self.headval = None
# # Function to add newnode

#     def removeDup(self):
#         if(self.headval is None):
#             return
#         hd = self.headval
#         while hd.nextval is not None:
#             # print(hd.dataval)
#             if hd.dataval == hd.nextval.dataval:
#                 new = hd.nextval.nextval
#                 hd.nextval = None
#                 hd.nextval = new
#             else:
#                 hd = hd.nextval

#                 # hd = hd.nextval

#             # hd = hd.nextval

#     def AtEnd(self, newdata):
#         NewNode = Node(newdata)
#         if self.headval is None:
#             self.headval = NewNode
#             return
#         laste = self.headval
#         while(laste.nextval):
#             laste = laste.nextval
#         laste.nextval = NewNode
# # Print the linked list

#     def listprint(self):
#         printval = self.headval
#         while printval is not None:
#             print(printval.dataval)
#             printval = printval.nextval


# list = SLinkedList()
# list.headval = Node("Mon")
# e2 = Node("Tue")
# e21 = Node("Tue")
# e3 = Node("Wed")

# list.headval.nextval = e2
# e2.nextval = e21
# e21.nextval = e3
# # e3

# list.AtEnd("Thu")

# list.listprint()
# print("=========")
# list.removeDup()
# print("=========")
# list.listprint()


# #!Dynamic programming withh recursion
# class Solution:
#     def climbStairs(self, n: int, dct={}) -> int:
#         if(n in dct):
#             return dct[n]
#         s = 0
#         if (n == 0):
#             return 1
#         elif(n < 0):
#             return 0
#         s += self.climbStairs(n - 1)+self.climbStairs(n - 2)
#         dct[n] = s

#         return s


# re = ''

# print(len(t)+1 % k)
# if(len(t) % k != 0):
#     t += i
# else:
#     t += "-"+i'


# def superDigit(n, k):
#     print(rec(int(str(n)*4), k))
#     return

# p =  list(n)
# return int(n[1])+superDigit(n[1:],len(n[1:]))
# Write your code here
# def superDigit(n, k):
#     # print(type(n))
#     if(len(str(n)) == 1):
#         return n
#     else:
#         t = 0
#         for h in str(n):
#             t += int(h)
#         return superDigit(t, len(str(t)))


# print(superDigit(int(str(9875)*4), 4))
# def permut(st):
#     if(len(st) == 0):
#         # st = re+st
#         return []
#     if(len(st) == 1):
#         # st = re+st
#         return [st]
#     else:
#         l = []
#         print(len(st))
#         for i in range(len(st)):
#             x = st[i]
#             xs = st[:i]+st[i+1:]

#             for j in permut(xs):
#                 l.append([x]+j)
#         return l

#         # if(len(re) % ng == 0):
#         #     re = re+",,"
#         #     return re
#         # else:
#         #     return re

# print(permut(list("abc")))
# from numpy import insert
# class Node:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.right = None
#         self.left = None
#     def insertD(self, data):
#         # if(self.data):
#         if(self.data):
#             print("Inside")
#             #!left
#             if(data < self.data):
#                 print("Left")
#                 if(self.left is not None):
#                     return self.left.insertD(data)
#                     # return
#                 else:
#                     if(self.data == data):
#                         return
#                     else:
#                         self.left = Node(data)
#                     # return
#             #!right
#             elif(data > self.data):
#                 print("Right")
#                 if(self.right is not None):
#                     self.right.insertD(data)
#                     # self.right = self.insertD(data)
#                     # return
#                 else:
#                     #!diasslow duplication
#                     if(self.data == data):
#                         return
#                     else:
#                         self.right = Node(data)
#             else:
#                 self.data = data
#                 # return
#         # return Node(data)
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print(self.data),
#         if self.right:
#             self.right.PrintTree()
#     global found
#     found = False
# t = Node(5)
# t.insertD(10)
# t.insertD(2)
# t.insertD(12)
# t.insertD(6)
# t.insertD(6)
# t.insertD(0)
# t.insertD(5)
# t.PrintTree()
# print(t.findTree(12))
# print()
"""

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None
# Print the linked list

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBegining(self, newdata):
        NewNode = Node(newdata)

# Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode


list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

list.AtBegining("Sun")
list.listprint()

"""


# class Node:
#     def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None


# class LinkedList:
#     def __init__(self) -> None:
#         self.headVal = None

#     def insertAtEnd(self, data):
#         n = self.headVal
#         #! At Beginning
#         # if(n is not None):

#         # if(self.headVal is None):
#         #     Node(data).nextval = self.headVal
#         #     self.headVal = Node(data)

#         #     return
#         # cur
#         #!last
#         n = self.headVal
#         while(n is not None):
#             cur = n
#             n = n.nextval
#         # cur =
#         cur.nextval = Node(data)
#         return

#     def atBeg(self, data):
#         n = self.headVal
#         newNode = Node(data)
#         # print(self.headVal)
#         # print(self.headVal.dataval)
#         #! self.headVal = [[][[]]]
#         newNode.nextval = self.headVal
#         #! self.headval = [newNode[][]]
#         self.headVal = newNode
#         # print(self.headVal)
#         # print(self.headVal.nextval)
#         return
#     #! with ll and index try

#     def atMiddile(self, currNode, data):
#         # newNode = Node(data)
#         # n = self.headVal
#         newn = Node(data)
#         newn.nextval = currNode.nextval
#         currNode.nextval = newn
#         return
#     #!with key and index

#     def remove(self, data):
#         # if()

#         n = self.headVal
#         if(n is not None):
#             if(n.dataval == data):
#                 self.headVal = n.nextval

#                 n = None
#                 return
#         while (HeadVal is not None):
#             if HeadVal.data == data:
#                 break
#             prev = HeadVal
#             HeadVal = HeadVal.next
#         prev.next = HeadVal
#         prev = None
#         # while(n is not None):
#         #     if(n.dataval == currNode.dataval):
#         #         print("========")
#         #         print(n.dataval)
#         #         break

#         #     n = n.nextval

#         # pass

#     def printLl(self):
#         p = self.headVal

#         while(p is not None):
#             print(p.dataval)
#             p = p.nextval


# ll = LinkedList()
# ll.headVal = Node(10)
# # ll.insert(10)
# ll.headVal.nextval = Node(15)
# ll.insertAtEnd(25)
# ll.atBeg(4)
# ll.printLl()
# print("===========")
# ll.atMiddile(ll.headVal.nextval, 6)
# ll.printLl()


# def binSearch():

# def sumofNatural(n):
#     if(n == 1 or n == 0):
#         return n
#     return n+sumofNatural(n-1)

# print(sumofNatural(5))
# def decToBin(numb):
#     if(numb == 0):
#         return ""
#     return decToBin(numb//2)+str(numb % 2)


# print(decToBin(233))

# 234 % 2 == rem 1
# 116% 2 =
# base case

# def st(yt):
#     if(len(yt) == 1 or len(yt) == 0):
#         return yt
#     return yt[-1]+st(yt[:-1])

# print(st(""))
# def pal(st):
#     if(len(st) == 0 or len(st) == 1):
#         return True
#     if(st[0] == st[-1]):
#         return pal(st[1:-1])
#     return False

# print(pal("reaer"))
