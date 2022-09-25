from turtle import Turtle
import random
# TODO 1: ADD MORE start headings
start_headings_right = [45, 120, 200, 315]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.round_heading = 45
        self.setheading(self.round_heading)
        self.move_speed = 0.1


    def move(self):
        self.forward(10)

    def wall_collision(self):
        print(self.ycor())
        if (self.ycor() > 285 and self.ycor() < 300) or (self.ycor() < -285 and self.ycor() > -300):
            print(self.ycor())
            return True
        else:
            return False

    def bounce_wall(self):
        self.setheading(360 - self.heading())
        self.forward(20)

    def bounce_paddle(self):
        self.setheading(180 - self.heading())
        self.forward(20)

    def restart(self):
        self.round_heading = 180 - self.round_heading
        self.setheading(self.round_heading)
        self.setposition(0, 0)

    def speed_up_ball(self):
        self.move_speed *= 0.9