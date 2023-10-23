import random
from turtle import Turtle , Screen

screen = Screen()
screen.setup(width=1000, height=700)
race_on = False
bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race?Enter the color: ")
colors = ["red", "blue", "yellow", "green", "orange", "indigo", "violet"]
y_pos = [-100, 0, -200, 100, 200, -300, 300]
turtles = []
for i in range(0, 7):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-480, y_pos[i])
    tim.pendown()
    turtles.append(tim)

if bet:
    race_on = True
while race_on:
    for i in turtles:
        i.penup()
        if i.xcor() > 480:
            race_on = False
            winning_color =  i.pencolor()
            if winning_color == bet:
                print(f"You've won!")
            else:
                print("You've lost the bet")
            print(f"{winning_color} turtle won the race.")
        distance = random.randint(0, 10)
        i.forward(distance)
screen.exitonclick()