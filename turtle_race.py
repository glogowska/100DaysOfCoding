from turtle import Turtle, Screen
import random


def lost_won(string1, string2):
    if string1 == string2:
        return "won"
    else:
        return "lost"


is_race_on = False
FINISH_LINE_X = 230.00
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
while True:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    if user_bet in colors:
        break

turtles = []
x = -230
y = -100
counter = 0

finish_drawer = Turtle()
finish_drawer.isvisible()
finish_drawer.penup()
finish_drawer.setposition(x=230.00, y=-110)
finish_drawer.pendown()
finish_drawer.left(90)
finish_drawer.forward(240)
for turtle in colors:
    turtles.append(Turtle(shape="turtle"))
    turtles[counter].color(colors[counter])
    turtles[counter].penup()
    turtles[counter].goto(x, y)
    turtles[counter].speed("fastest")
    counter += 1
    y += 40

race_is_on = True
finished_turtles = 0
winning_turtles = []
while race_is_on:
    for turtle_index1 in range(0, 6):
        if turtles[turtle_index1].xcor() >= FINISH_LINE_X and turtles[turtle_index1].color()[1] not in winning_turtles:
            finished_turtles += 1
    if finished_turtles == 6:
        break
    else:
        for turtle_index2 in range(0, 6):
            if turtles[turtle_index2].xcor() >= FINISH_LINE_X:
                winning_turtles.append(turtles[turtle_index2].color()[1])
            if turtles[turtle_index2].xcor() < FINISH_LINE_X:
                steps = random.randint(0, 5)
                turtles[turtle_index2].forward(steps)

print(f"You {lost_won(winning_turtles[0], user_bet)}. You chose {user_bet}. "
      f"The turtle that won is {winning_turtles[0]}.")


screen.exitonclick()
