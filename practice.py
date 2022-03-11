import random

print(random.random())
x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
# !
# Built In data types
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# !
# def myfunc():
#     global x
#     x = "fantastic"


# myfunc()
# print("Python is " + x)
x = dict(name="John", age=36, hel=45)
x["get"] = "hell"
print(x)
x = bool(5 == 5)
print(x)
x = bytes(5)
print(x)
print(35e3)
# ! Strings are Arrays
txt = "The best things in life are free!"
print("free" in txt)
txt = "The best things in life are free!"
print("expensive" not in txt)
b = "Hello, World!"
print(b[-5:-2])
