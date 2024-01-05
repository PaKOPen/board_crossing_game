import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10

class CarManager(Turtle):

    def __init__(self):
        self.cars = []
        self.STARTING_MOVE_DISTANCE = 5

    def create_car (self):
        random.chance = random.randint(1,6)
        if random.chance == 1:
            new_car = Turtle('square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(350, random_y)
            self.cars.append(new_car)

    def moving_car(self):
        for car in self.cars:
            car.backward(self.STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.STARTING_MOVE_DISTANCE += MOVE_INCREMENT