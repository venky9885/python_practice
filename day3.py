
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


# * Method	Description ---List Methods----------
# *append()	Adds an element at the end of the list
# *clear()	Removes all the elements from the list
# *copy()	Returns a copy of the list
# *count()	Returns the number of elements with the specified value
# *extend()	Add the elements of a list (or any iterable), to the end of the current list
# *index()	Returns the index of the first element with the specified value
# *insert()	Adds an element at the specified position
# *pop()	Removes the element at the specified position
# *remove()	Removes the item with the specified value
# *reverse()	Reverses the order of the list
# *sort()	Sorts the list
l = [1, 2, 3, 5, 5]
print(l[1:3])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#! 1
thislist.insert(2, "watermelon")
thislist.insert(2, "banana")
#! 2
thislist.remove("banana")
#! 3
thislist.pop(1)
#! 4
del thislist[0]
thislist.clear()
#! 5
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
print(thislist)
######**********####################
print("SORtINg##############33333")
# Example
#! Sort the list based on how close the number is to 50:


def myfunc(n):
    return abs(n - 50)
# 50, 0, 15 ,32,27
# 100 ,50, 65,82,23
#


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)

print(thislist)
##############!#####################
#! 6


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]
nl = [x if x != "bn" else "or" for x in fruits]


# *****************************************************************************TUPLES********************************
#! Ordered
#! Unchangable (Immutable) ---Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#! Allow Duplicates


# creation
("apple",)
# length
len(tuple)
# access(same methd as in list)
tuple[0]
# No Update
# No remove
#! .count()
#! .index()
#! Unpacking
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
#!----------------|----------------= ("cherry", "strawberry", "raspberry")
print(green)
print(yellow)
print(red)

# ***********************  SETS **********************
# {}
# .add()
# .update()
# .remove(),.discard("banana")
# .pop()
# .clear()


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
