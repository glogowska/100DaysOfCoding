from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

sleeping_time = 0.1

screen = Screen()

screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Game Of Pong")
screen.tracer(0)
score_board = ScoreBoard()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    if ball.wall_collision() == False:
        ball.move()
    else:
        ball.bounce_wall()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_paddle()
    elif ball.xcor() > 390:
        ball.restart()
        score_board.add_point_left()
        ball.speed_up_ball()
    elif ball.xcor() < -390:
        ball.restart()
        score_board.add_point_right()
        ball.speed_up_ball()

screen.exitonclick()
