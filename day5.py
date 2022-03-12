class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)

# * With self


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# * object craetion
p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# * With function


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()
#! Inheritance


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:


x = Person("John", "Doe")
x.printname()

#!|
#!V


class Student(Person):
    pass


x = Student("Mike", "Olsen")
x.printname()


class Student(Person):
    def __init__(self, fname, lname):
        pass
        # add properties etc.
        #!When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

        # *To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

        # * Example


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


#! Super Function
# Use the super() Function
# *Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

# ***************************** Super function with examplre -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-**--*------

#! Parent


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# * Child


class Student(Person):
    #! If you use __init__ here then Child no longer inherit  propertirs from parents
    # * the child class will no longer inherit the parent's __init__() function.
    def __init__(self, fname, lname, year):
        #! Must call the super for sake of parent fubction
        super().__init__(fname, lname)
        self.graduationyear = year


x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)
