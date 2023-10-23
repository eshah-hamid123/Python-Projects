# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)
import random
import turtle as t
timmy = t.Turtle()
t.colormode(255)
color_list = [(139, 164, 184), (27, 114, 171), (202, 141, 167), (237, 213, 67), (219, 157, 89), (22, 136, 66), (139, 21, 37), (124, 72, 94), (185, 176, 26), (70, 30, 37), (182, 73, 41), (225, 170, 197), (52, 36, 34), (232, 83, 40), (39, 174, 99), (108, 190, 136), (9, 107, 64), (29, 169, 185), (181, 95, 112), (38, 37, 43), (239, 216, 8), (188, 184, 210), (158, 207, 215), (152, 214, 174), (240, 169, 154), (105, 41, 39)]
timmy.speed('fastest')
timmy.penup()
timmy.hideturtle()
timmy.setheading(180)
timmy.forward(300)
timmy.left(90)
timmy.forward(300)
timmy.left(90)
for i in range (10):
    for j in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.setheading(0)
    # timmy.setheading(90)
    # timmy.forward(50)
    # timmy.setheading(180)
    # timmy.forward(500)
    # timmy.setheading(0)


screen = t.Screen()
screen.exitonclick()
