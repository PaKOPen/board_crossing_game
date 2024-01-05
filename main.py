import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
my_turtle = Player()

screen.listen()
busy_road = CarManager()
score = Scoreboard()

screen.onkey(my_turtle.move_forward, "Up")
screen.onkey(my_turtle.move_left, "Left")
screen.onkey(my_turtle.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    busy_road.create_car()
    busy_road.moving_car()

    for car in busy_road.cars:
        if car.distance(my_turtle) < 20:
            game_is_on = False
            score.game_over()


    if my_turtle.is_at_finish():
        my_turtle.goto_start()
        score.completed_crossing()
        busy_road.increase_speed()

screen.exitonclick()