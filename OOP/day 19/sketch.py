from turtle import Turtle , Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_counterclockwise():
    tim.left(40)


def move_clockwise():
    tim.right(40)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def movement():
    screen.onkey(fun=move_forward, key='W')
    screen.onkey(fun=move_backward, key='S')
    screen.onkey(fun=move_counterclockwise, key='A')
    screen.onkey(fun=move_clockwise, key='D')
    screen.onkey(fun=clear_screen, key='C')


screen.listen()

draw = True
while draw:
    movement()
    if screen.exitonclick():
        draw = False