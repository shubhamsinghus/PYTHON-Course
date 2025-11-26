
#   def __init__(self,brand,):
#      self.brand= brand
#   def price(self):
#       return "Around 20 lakhs"
# class Honda(Car):
#
#
#  def __init_(self,price):
#      self.price=price


#  #objcreation
# obj_price=Car("mahindra",1500000)
# ob2=THAR(6000000)
# print(THAR().obj_price())
#

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some generic animal sound"

# Derived class 1
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return "Woof! Woof!"

# Derived class 2
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        return "Meow! Meow!"

# Polymorphism in action
animals = [Dog("Buddy", "Golden Retriever"), Cat("Whiskers", "White")]

for animal in animals:
    print(f"{animal.name} says: {animal.sound()}")

from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())

 #method overloading
# Define a class Calculator.
class Calculator:
    def add(self, a, b, c = 0):
        return a + b + c

# Create an instance of class Calculator.
calc = Calculator()

# Call add() method using reference variable calc by passing differnt number of arguments.
# Store the results into variables result1 and result2.
result1 = calc.add(1, 2)      # Calls add with 'c' defaulting to 0.
result2 = calc.add(1, 2, 3)   # Calls add with 'c' set to 3.

# Display the results on the console.
print(result1)
print(result2)

 # method overriding

# Define a base class.
class Shape:
    def area(self):
        pass

# Define derived classes.
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Outside the class definition.
sq = Square(20)
rc = Rectangle(10, 20)
cr = Circle(3)

# Calling the overriding methods of derived classes.
print("Area of square: ", sq.area())
print("Area of rectangle: ", rc.area())
print("Area of circle: ", cr.area())

#adittion operaters
num1 = 20
num2 = 30
print(num1 + num2)

str1 = "Python"
str2 = " Programming"
print(str1 + str2)
 #class method in python
class Jharkhand:
    def capital(self):
        print("Ranchi")
    def language(self):
        print("Hindi and English")

class Bihar:
    def capital(self):
        print("Patna")
    def language(self):
        print("Hindi and English and Bhojpuri")

# Creating objects.
obj1 = Jharkhand()
obj2 = Bihar()

# Use for loop to access different objects.
for state in (obj1, obj2):
    state.capital()
    state.language()
 #with duck typing
class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


def make_sound(animal):
    print(animal.speak())

    # Creating objects.


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)
 #functions polymerphism
# Python program to illustrate the polymorphism in len() function.
# This statement will determine the length of the string.
print(len("Python Programming"))

# This statement will determine the number of items.
print(len(["Java", "HTML", "Python", "JavaScript"]))

# This statement will determine the total number of keys.
print(len({"Name": "Deepak", "Address": "Dhanbad"}))
 #polymerphisms with function object
# Python program to demonstrate the polymorphism with functions and objects.
# Create a class named India.
class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi and English are the most widely spoken languages of India.")
    def type(self):
        print("India is a developing nation.")

# Create a class named USA with the same method names as in the class India.
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
    def language(self):
        print("English is the primary language of USA.")
    def type(self):
        print("USA is a developed country.")

# Define a function called 'func' that takes an object 'obj' as an argument
def func(obj):
  # Call methods of the provided object.
    obj.capital()
    obj.language()
    obj.type()

# Create an instance of the 'India' class and store it in 'obj_ind'.
obj_ind = India()
# Create an instance of the 'USA' class and store it in 'obj_usa'.
obj_usa = USA()

# Call the 'func' function with 'obj_ind' as the argument.
func(obj_ind)
# Call the 'func' function with 'obj_usa' as the argument.
func(obj_usa)


classA:
 def func(obj):
