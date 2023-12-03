from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.highscore = (data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()




