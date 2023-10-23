from turtle import Screen
import turtle as t
import random


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


timmy = t.Turtle()
t.colormode(255)
timmy.speed('fastest')


def spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


spirograph(3)
screen = Screen()
screen.exitonclick()