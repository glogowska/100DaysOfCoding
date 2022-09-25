from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 70, "normal"))

    def add_point_left(self):
        self.l_score += 1
        self.update_score_board()

    def add_point_right(self):
        self.r_score += 1
        self.update_score_board()
