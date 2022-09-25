from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.right(90)
        self.goto(position)


    def up(self):
        if self.ycor() < 250:
            self.backward(10)

    def down(self):
        if self.ycor() > -250:
            self.forward(10)
