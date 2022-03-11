age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity, itemno, price))
# ! Escape "We are the so-called \"Vikings\" from the north."
x = "hEllo"
print(x.casefold())  # complete lolwer case
print(x.capitalize())  # start upper case
print(x.center(20, "*"))  # center string between 20 char
print(x.count("l"))  # count the number of l in the string
print(x.encode())  # encode the string
print(x.startswith("o"))  # check if the string starts with the specified value
print(x.endswith("o"))  # check if the string ends with the specified value
print(x.expandtabs(20))  # set the tab size of the string
# search the string for a specified value and returns the position of where it was found -2(find and index are same)
print(x.find("l"))
print(x.index("l"))
print(x.isalnum())  # Returns True if all characters in the string are alphanumeric
print(x.isdigit())

# ! islower(), isupper()

# myTuple = ("John", "Peter", "Vicky")

# x = "#".join(myTuple)

# print(x)

print(x.replace("l", "8"))
print(x.swapcase())
print(x.title())  # Converts the first character of each word to upper case
# Fills the string with a specified number of 0 values at the beginning#
print(x.zfill(10))
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)


# ! rjust
txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")
# !output  (right side text)
#!             banana is my favorite fruit.
#! ljust
txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")
# !output(left side text)
#! banana               is my favorite fruit.

txt = "banana"

x = txt.rjust(20, "O")

print(x)
# !OOOOOOOOOOOOOObanana
