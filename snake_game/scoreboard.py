from turtle import Turtle
with open("data.txt", mode="r") as file:
    HIGH_SCORE = file.read()
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
        self.high_score = int(HIGH_SCORE)

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)

    def add_point(self):
        self.score += 1
        self.display_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                self.score = file.write(f"{self.high_score}")
        self.score = 0
        self.display_score()

    # def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)
