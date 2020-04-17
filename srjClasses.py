x = 1
print(type(x))

x = "Saran"
print(type(x))

# Everything in Python is a class

# methods and parameters
def hello(name):
    print("hello",name)

hello("Saran")

# Strings

string = "hello"
print(string.upper())


# Class


class Dog:
    def bark(self):
        print("bark")

d = Dog()  # d is an object that contains an instance of the class Dog

d.bark()  #prints the bark
print(type(d))  # it prints <class '__main__.Dog'>

# Class is a common blueprint/Template
# Class may contains some variables and methods
# Whenever you call the class then an instance of class/Runtime of the class is getting created
# Class => user calls => It becomes Instance(run time of class)
# Instance contains all methods and variables of the class
# If an instance is filled with user inputs then its called an object
# We cannot directly execute a class so we have to create an object first and through an object we can access all methods and variables in a class

# reason for creating classes is that to reduce the number of lines and code reusability

# init methods:

class Dog:
    def __init__(self,name):
        print(name)

d = Dog("rocky") # prints rocky

# constructor is called init methods and it executes during the object creation or instnace creation
# use of self, it grabs the user input and pass it to all methods and attributes in a class

class Dog:
    def __init__(self,name):
        self.DogClassName = name
        print(self.DogClassName)

d = Dog("danny") # prints rocky

# return provides some value back to the class
class Dog:
    def __init__(self,name):
        self.DogClassName = name

    def printdogname(self):
        return self.DogClassName
d = Dog("danny") # prints rocky
print(d.printdogname())














