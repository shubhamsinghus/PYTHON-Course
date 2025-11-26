# def sum ():
#     a=int(input("enter the first number :"))
#     b=int(input("enter the second number:"))
#     c=a+b
#     print(c)
#
#
#
#
# sum()
# def product(a,b):
#    a=int(input("enter the first number :"))
#    b=int(input("enter the second number:"))
#    product=a*b
#    return product
#    print(product)
# n = int(input("enter any no:"))
# if n % 2 != 0:
#     print("wired")
# elif 2 <= n <= 5:
#     print("Not wired")
# elif 6 <= n <= 20:
#     print("wired")
# elif n > 20 and n % 2 == 0:
#
#     print("Not wired")

# def product(x,y):
#     product=x*y
#     return product
# x=int(input("Enter a number x: "))
# y=int(input("Enter another number y: "))
# ans=product(x,y)
# print("The product of two numbers is",ans)

# def expo(x,y):
#     expo = x ** y
#     return expo
# x=int(input("Enter a number x: "))
# y=int(input("Enter another number y: "))
# ans=expo(x,y)
# print("X to the power Y",ans)

#prime numbers
# def is_prime(n):
#     if n<=1:
#      return False
#     if n==2:
#         return True
#     for i in range(3,n):
#         if n % i ==0:
#          return False
#     return True
#
# n=int(input("Enter any number :"))
# if is_prime(n):
#     print(n,"is a prime number")
# else:
#     print(n,"is not a prime number")

#area of sphere
# def area(r):
#     area=4*(3.14* r**2)
#     return area
#
# r=int(input("Enter the radius of the sphere:"))
# print("The area of given sphere is:",area(r))

# fACTORIAL OF NUMBER
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# n=int(input("enter a number:"))
# print("factorial of ", n, "is:" ,factorial(n))

# #def is_prime(n):
#     if n <= 1:
#         return False   # 0 and 1 are not prime
#     if n == 2:
#         return True    # 2 is prime
#     if n % 2 == 0:
#         return False   # any even number > 2 is not prime

#     # check odd divisors
#     for i in range(3, n):
#         if n % i == 0:
#             return False
#     return True

# # Example
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(num, "is a prime number")
# else:
#


#flatten list using recursion
# li=[1,2,[1,2,3],4,5,[4,5,6,7,8,3],4,5]
# li=1,2,3,1,2,3,4,5,4,5,6,7,8,3,4,5]


# def flatten(li):
#      for i in li:
#         if  type(i) == int:
#             print(i)
#
#         else:
#             print(list)
#             flatten(i)
#
# li=[1,2,3,[1,2,3],4,5,[4,5,6,7,8,3],4,5]
# flatten(li)
# import turtle
#
# # Setup
# t = turtle.Turtle()
# turtle.bgcolor("black")
# t.color("cyan")
# t.pensize(8)
# t.speed(2)

# Function to move without drawing
# def move(x, y):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#
# # Draw R
# move(-250, 0)
# t.left(90)
# t.forward(100)
# t.right(90)
# t.circle(-25, 180)
# t.left(90)
# t.forward(50)
# t.right(135)
# t.forward(70)
# t.left(135)

# # Draw O
# move(-150, 0)
# t.circle(50)
#
# # Draw H
# move(-30, 0)
# t.left(90)
# t.forward(100)
# t.backward(50)
# t.right(90)
# t.forward(50)
# t.left(90)
# t.forward(50)
# t.backward(100)
#
# # Draw I
# move(70, 0)
# t.left(90)
# t.forward(100)
# t.backward(100)
#
# # Draw T
# move(150, 100)
# t.forward(60)
# t.backward(30)
# t.right(90)
# t.forward(100)
#
# t.hideturtle()
# turtle.done()
n=int(input("enter any no:"))
def square(n):
  C=n**2
  print(C)
for i in range(5):
    square(i)