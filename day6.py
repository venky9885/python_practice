import math
x = "h"
try:
    print(x)
except:
    print("An exception occurred")

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
#! Raise Exceptions
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
x = math.sqrt(64)

print(x)


x = math.ceil(1.4)
y = math.floor(1.4)

print(x)  # returns 2
print(y)  # returns 1
x = math.pi


dict_comprehension = {key: val for key, val in enumerate('sample')}
print(dict_comprehension)
for num, fruit, thing in zip([1, 2, 3], ['apple', 'grape', 'orange'], ['x', 2, True]):
    print(num)
    print(fruit)
    print(thing)
