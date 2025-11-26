# import turtle
# pattern=turtle.Turtle()
# wn = turtle.Screen()
# wn.bgcolor("blue")
# wn.title("Turtle")
import sys
from unittest import main

# for k in range(0,50, 10):
#     for i in range(3):
#         pattern.forward(120+k)
#         pattern.right(120)
#     pattern.backward(30+k)
#turtle.done()

#import turtle

# t = turtle.Turtle()
# t.speed(10)
# for i in range(5):
#     t.forward(100)
#     t.right(144)
#
# turtle.done()


# import turtle
# colors=["red","blue","yellow","green","purple"]
# t=turtle.Turtle()
# t.speed(5)
# for i  in range(60):
#     t.color(colors[i%6])
#     t.forward(i * 5)
#     t.right(59)
#
# turtle.done()
# import turtle
#
# colors = ["red", "blue", "green", "orange", "purple", "yellow"]
# t = turtle.Turtle()
# t.speed(0)
# win=turtle.Screen()
# win.bgcolor("black")
#
# for i in range(60):
#     t.color(colors[i % 6])
#     t.forward(i * 5)
#     t.right(225)
#
# turtle.done()

# import turtle
#
# t = turtle.Turtle()
# t.speed(0)
# t.width(1)
# turtle.bgcolor("black")
# colors = ["#00FFFF", "#00FF99", "#FF00FF", "#FF6600"]
#
# for i in range(60):
#     t.color(colors[i % 4])
#     t.circle(100)
#     t.right(6)
#     t.forward(5)
#
# # t.hideturtle()
# # turtle.done()
# # import turtle
# # t=turtle.Turtle()
# # t.shape("turtle")
# # t.speed(0)
# # t.width(5)
# # turtle.bgcolor("black")
# # colors = ["red","green","blue","yellow","magenta","cyan","orange","pink"]
# # for i in range(90):
# #     t.color(colors[i%8])
# #     t.forward(160)
# #     t.right(145)
# # t.hideturtle()
# # turtle.done()
# import turtle
# import colorsys
#
# t = turtle.Turtle()
# turtle.bgcolor("black")
# t.speed(0)
# t.width(2)
# t.hideturtle()
#
# # Generate rainbow-like colors
# n = 36
# h = 0
# for i in range(360):
#     c = colorsys.hsv_to_rgb(h, 1, 1)
#     h += 1 / n
#     t.color(c)
#
#     t.circle(180)
#     t.right(10)
#     for j in range(4):
#         t.right(45)
#         t.circle(100, 90)
#
# turtle.done()
# import turtle
# import colorsys
# import time
#
# # Setup
# t = turtle.Turtle()
# t.speed(0)
# t.width(2)
# t.hideturtle()
# turtle.bgcolor("black")
#
# # Color setup
# n = 36  # number of hues
# h = 0
#
# # Animation loop
# for i in range(72):  # number of layers
#     c = colorsys.hsv_to_rgb(h, 1, 1)
#     h += 1 / n
#     t.color(c)
#
#     # Draw one circular pattern
#     t.circle(100)
#     t.right(10)
#
#     # Inner glow effect
#     for j in range(4):
#         t.circle(100)
#         t.right(90)
#
#     # Short pause for smooth animation
#     time.sleep(0.05)
#
# turtle.done()

# import turtle
# wn = turtle.Screen()
# wn.bgcolor("lightblue")
# t = turtle.Turtle()
# t.pensize(5)
# t.penup()
# t.goto(-300,0)
# t.pendown()
# t.speed(10)
# t.right(320)
# t.forward(100)
# t.right(90)
# t.forward(90)
# t.backward(50)
# t.left(50)
# t.backward(60)
# turtle.done()

# import turtle
# window = turtle.Screen()
# window.bgcolor("lightblue")
# t=turtle.Turtle()
# t.speed(5)
# t.pencolor("red")
# t.pensize(10)
# t.penup()
# t.goto(-300,-100)
# t.pendown()
# t.left(90)
# t.forward(250)
# t.right(90)
# t.forward(50)
# t.circle(-60,225)
# t.left(160)
# t.forward(150)
# # Draw O
# t.penup()
# t.goto(-150, -50)
# t.pendown()
# t.circle(100)
#
#
#
# turtle.done()


#
