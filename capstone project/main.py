import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_car()
    if player.ycor() > 280:
        player.refresh()
        car.increment_speed()
        scoreboard.level()
    for cars in car.all_cars:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
