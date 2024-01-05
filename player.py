from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(). __init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape('turtle')
        self.setheading(90)
        # self.

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish (self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
