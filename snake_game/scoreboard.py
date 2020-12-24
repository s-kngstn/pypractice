from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 13, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.score = 0

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}",
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)

    def add_point(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
