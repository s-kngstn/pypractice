from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    '''Player controled paddle to hit ball'''
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.color("white")

    def go_up(self):
        '''Moves paddle up / forward'''
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        '''Moves paddle down / backward'''
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
