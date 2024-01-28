from turtle import Turtle

with open("Data.txt") as data:
    High = data.read()


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(High)
        self.color("White")
        self.penup()
        self.sety(285)
        self.setx(0)
        self.write(f'Score = {self.score} High score = {self.high_score} ', True, 'center', ('Arial', 10, 'normal'))
        self.hideturtle()

    def current_score(self):
        self.clear()
        self.sety(285)
        self.setx(0)
        self.write(f'Score = {self.score} High score = {self.high_score} ', True, 'center', ('Arial', 10, 'normal'))

    def Scores(self):
        self.clear()
        self.score += 1
        self.sety(285)
        self.setx(0)
        self.write(f'Score = {self.score} High score = {self.high_score} ', True, 'center', ('Arial', 10, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Data.txt", mode="w") as data:
                data.write(str(self.score))
        self.score = 0
