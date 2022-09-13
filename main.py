from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
screen = Screen()


def move_forward():
    turtle.forward(10)


def turn_right():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)


def turn_left():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)


def draw_backwards():
    turtle.backward(10)


def draw_circle():
    turtle.circle(120, 10)


def clear_screen():
    turtle.reset()


screen.listen()
screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=turn_right, key="d")
screen.onkeypress(fun=turn_left, key="a")
screen.onkeypress(fun=draw_backwards, key="s")
screen.onkeypress(fun=clear_screen, key="c")


screen.exitonclick()
