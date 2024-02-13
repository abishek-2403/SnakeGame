from turtle import Turtle
ALIGN = "Center"
FONT = ("Arial", 15, "normal")

with open("score_data.txt", mode="r") as file:
    HIGH_SCORE = int(file.read())

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.high_score = HIGH_SCORE
        self.write_score()
        self.scores = []

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score_data.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.write_score()


    def update_score(self):
        self.score += 1
        self.write_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGN, font=FONT)

