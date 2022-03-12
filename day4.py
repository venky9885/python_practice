# #***********************************Dictionaroies*****************************


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])
print(len(thisdict))
x = thisdict.values()
x = thisdict.keys()
x = thisdict.items()
thisdict.update({"year": 2020})
# Add
thisdict["color"] = "red"
thisdict.pop("model")
thisdict.popitem()
# renoves k=last one
thisdict.clear()


# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

a = 100
b = 200
if a > b:
    print("a is greater than b")
print("A") if a > b else print("B")
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
# Example
# If the number of arguments is unknown, add a * before the parameter name:
#! *kwargs tuple  tp[0]


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")

# default args


def my_function(country="Norway"):
    print("I am from " + country)
# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# Example
# If the number of keyword arguments is unknown, add a double ** before the parameter name:

#! **kwargs Dictionary


def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


#! lamda
def x(a): return a + 10


# x = lambda a : a + 10
# print(x(5))
# x = lambda a, b : a * b
# print(x(5, 6))
print(x(5))
# !The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unkn


def myfunc(n):
    return lambda a: a * n


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))
# * Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
