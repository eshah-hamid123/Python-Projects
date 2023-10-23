import turtle as t
from turtle import Screen
import random


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


timmy = t.Turtle()
t.colormode(255)
timmy.shape('arrow')
no = 3
not_decagon = True
while not_decagon:
    timmy.color(random_color())
    for i in range(no):
        angle = 360 / no
        timmy.forward(100)
        timmy.right(angle)
    no+=1
    if no == 11:
        not_decagon = False

screen = Screen()
screen.exitonclick()