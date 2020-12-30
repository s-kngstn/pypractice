from turtle import Turtle
FONT = ("Courier", 18, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-230, 260)
        self.score = 0

    def display_score(self):
        self.clear()
        self.write(f"Level: {self.score}",
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)

    def add_point(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
