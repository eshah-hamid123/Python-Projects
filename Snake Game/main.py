from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game ")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.turtles[0].xcor() > 280 or snake.turtles[0].xcor() < -280 or snake.turtles[0].ycor() > 280 or snake.turtles[0].ycor() < -280:
        # scoreboard.reset()
        # snake.reset()
        game_on = False
        scoreboard.game_over()

    for segment in snake.turtles[1:]:
        if snake.turtles[0].distance(segment) < 10:
            # scoreboard.reset()
            # snake.reset()
            game_on = False
            scoreboard.game_over()
screen.exitonclick()
