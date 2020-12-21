from turtle import Turtle
import random

FOOD_COLOR = ["orange", "blue", "yellow", "green", "red", "purple"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()   

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.color(FOOD_COLOR[random.randint(0, len(FOOD_COLOR) - 1)])
        self.goto(random_x, random_y) 

    