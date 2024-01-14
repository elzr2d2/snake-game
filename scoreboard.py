from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 36, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
