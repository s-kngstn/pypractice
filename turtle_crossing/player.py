from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    '''Player Controlled Turtle'''
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.starting_position = STARTING_POSITION
        self.goto(STARTING_POSITION)
        self.finish_line = (0, FINISH_LINE_Y)

    def move_up(self):
        '''Moves player forward'''
        self.forward(MOVE_DISTANCE)
