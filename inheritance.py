# # single inheritance
#
# class books():
#     def order(self):
#         print("order books")
#     def exchange(self):
#         print("return books")
# class english(books):
#     def writer(self):
#         print("shubham singh")
#     def chap(self):
#         print("50  chapters")
#
# obj1 = books()
# obj2=english()
# obj2.chap()
# obj2.writer()
# obj2.exchange()
#

#multilevel
# class books():
#     def order(self):
#         print("order books")
#     def exchange(self):
#         print("return books")
# class genre(books):
#     def writer(self):
#         print("shubham singh")
#     def chap(self):
#         print("50  chapters")
# class language(genre):
#     def hindi(self):
#         print("hindi")
#     def english(self):
#         print("english")
# class price(language):
#     def price1(self):
#         print(" RS-200")

# prc =price()
# prc.price1()
# prc.chap()
# prc.order()
#
# lang=language()
# lang.writer()
#

# obj1 = books()
# obj2=language()
# obj3=price()
#
# obj2.chap()
# obj2.writer()
# obj2.exchange()
# obj3.price1()

 #MULTIPLE

# class A:
#     def order(self):
#         print("order books")
#     def exchange(self):
#         print("return books")
# class B:
#     def writer(self):
#         print("shubham singh")
#     def chap(self):
#         print("50  chapters")
# class C:
#     def hindi(self):
#         print("hindi")
#     def english(self):
#         print("english")
# class D(A,B,C):
#     def price1(self):
#         print(" RS-200")
# obj_d=D()
# obj_d.writer()
#hierarical
# class A:
#     def order(self):
#         print("order books")
#     def exchange(self):
#         print("return books")
# class B(A):
#     def order(self):
#         print("order books")
#     def writer(self):
#         print("shubham singh")
#     def chap(self):
#         print("50  chapters")
# class C(A):
#     def hindi(self):
#         print("hindi")
#     def english(self):
#         print("english")
# class D(A):
#     def price1(self):
#         print(" RS-200")

# obj_d=D()
# obj_d.price1()
# obj_d.exchange()

#hybrid
# class school():                   # single inheritance
#     def school(self):
#         print("school")
# class  principle(school):
#  def principle(school):
#   print("Principle")             # multilevel inheritance
# class teacher(principle):
#     def teacher(self):
#       print ("teacher")
# class math_teacher(teacher):          #multiple inheritance
#     def math_teacher(self):
#         print("math teacher")
# class computer_teacher(teacher):
#     def computer_teacher(self):
#         print("computer teacher")
# class english_teacher(teacher):
#     def english_teacher(self):
#         print("english teacher")
# class student(math_teacher, computer_teacher, english_teacher):
#     def student(self):
#         print("student")
# class sumit(student):
#     def sumit(self):
#         print("sumit")                              ##hierarical
# class shubham(student):
#     def shubham(self):
#         print("shubham")
# class Rohit(student):
#     def Rohit(self):
#         print("Rohit")
# class Komal(student):
#     def komal(self):
#         print("komal")
#
#
#
# stu_shubh= shubham()
# stu_rohit= Rohit()
# stu_komal= Komal()
# stu_shubh.principle()
# stu_rohit.teacher()
# stu_shubh.math_teacher()
#
#
# class Shape:
#     def area(self):
#         return "6"
# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length*self.width
#
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
# class Triangle(Shape):
#     def __init__(self,ci):
#         self.radius2=radius2
#
#     def area(self):
#             return 3.14*self.radius**2
#             return2 3.14*self.radius2**2
#
# shapes=[Rectangle(2,3),Circle(5)]
# for shape in shapes:
#         print("area of shape.area()",shape.area())
# class hunter:
#     def __init__(self,rifle,traps,supplies):
#         self.rifle = rifle
#         self.traps = traps
#         self.supplies = supplies
# inventory = hunter('barret-089','bear traps','canfood')
# print(inventory.rifle,inventory.traps,inventory.supplies)

# #class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# # p1 = Person("Alice", 30)
# # p2 = Person("Bob", 25)
#
# print(p1.name, p1.age)  # Alice 30
# print(p2.name, p2.age)  # Bob 25

#simple

# class Dog:
#     def __init__(self,name,age,breed ):
#         self.name = name
#         self.age = age
#         self.breed= breed
# class puupy(Dog):
#     def __init__(self,name,age,breed,character):
#         super().__init__(name,age,breed)
#         self.character = character
# tommy=Dog('Tommy',8,'black labrador')
# tiger=puupy('Tiger',3,'no breed','aggressive')
# print(tommy.name,tommy.age,tommy.breed)
# print(tiger.name,tiger.age,tiger.character)
#

#multilevel
#cat family
class leopard:
    def __init__(self,eye_colour,walking_pattern):
        self.eye_colour = eye_colour
        self.walking_pattern = walking_pattern
class cheetah:
   def __init__(self,eye_colour,walking_pattern,running_speed):
        self.running_speed = running_speed
class cat(leopard, cheetah):
    def __init__(self,eye_colour,walking_pattern,running_speed,skin_colour):
        super().__init__(eye_colour=eye_colour,walking_pattern=walking_pattern,running_speed)
        self.skin_colour = skin_colour

cat_char=cat('red','walking',34,'blackandwhite')
print(cat_char.running_speed,cat_char.skin_colour)

# class Leopard:
#     def __init__(self, eye_colour, walking_pattern, breed, **kwargs):
#         super().__init__(**kwargs)   # pass unused args forward
#         self.eye_colour = eye_colour
#         self.walking_pattern = walking_pattern
#         self.breed = breed
#
# # class Cheetah:
# #     def __init__(self, running_speed, **kwargs):
# #         super().__init__(**kwargs)   # pass unused args forward
# #         self.running_speed = running_speed
# #
# # class Cat(Leopard, Cheetah):   # Multiple inheritance
# #     def __init__(self, eye_colour, walking_pattern, breed, running_speed, skin_colour):
# #         super().__init__(eye_colour=eye_colour,
# #                          walking_pattern=walking_pattern,
# #                          breed=breed,
# #                          running_speed=running_speed)
# #         self.skin_colour = skin_colour
# #
# # # Create object
# # cat_char = Cat('red', 'walking', 'wild', 120, 'black')
# #
# # # Print attributes
# # print(cat_char.eye_colour, cat_char.walking_pattern, cat_char.breed,
# #       cat_char.running_speed, cat_char.skin_colour)
# #
# #
# #
# #
# #
# #
# #
#
#
