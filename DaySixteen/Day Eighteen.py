import turtle
import random
from turtle import *


def square_dashed():
    for fun in range(4):
        for _ in range(4):
            alfred.forward(25)
            alfred.pu()
            alfred.forward(25)
            alfred.pd()
            alfred.forward(25)
        alfred.left(90)
    alfred.home()
    turtle.clearscreen()


def triangle():
    for i in range(3):
        forward(100)
        right(120)


def hexagon():
    for i in range(5):
        forward(100)
        right(72)


def heptagon():
    for i in range(6):
        forward(100)
        right(60)


def octagon():
    for i in range(8):
        forward(100)
        right(45)


def nonagon():
    for i in range(9):
        forward(100)
        right(40)

def decagon():
    for i in range(10):
        forward(100)
        right(36)


alfred = Turtle()
turtle.colormode(255)
turtle.screensize(2000, 2000)

# position 55


def setup():
    turtle.pu()
    right(90)
    forward(550)
    right(90)
    forward(55)
    right(180)


while True:
    setup()
    break

# while True:
#     for i in range(100):
#         red = random.randint(0, 255)
#         green = random.randint(0, 255)
#         blue = random.randint(0, 255)
#         rgb = (red, green, blue)
#         turtle.pencolor(rgb)
#         turtle.width(10)
#         turtle.shapesize(3)
#
#         steps = int(random.random() * 100)
#
#         angles = (0, 90, 180, 270)
#         angle = random.choice(angles)
#
#         setheading(angle)
#         forward(steps)

    # if abs(pos()) < 1:
    #     break



turtle.exitonclick()
