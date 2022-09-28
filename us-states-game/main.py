import turtle
import pandas
FONT = ('Arial', 8, 'normal')
ALIGN = "center"
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()


# x and y values of the states, already logged in a csv file
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)


def write_a_state(state_name):
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    # state_row = data[data.state == state_name]
    # print(int(state_row.x))
    state.goto(int(data[data.state == state_name].x), int(data[data.state == state_name].y))
    state.write(state_name, align=ALIGN, font=FONT)

state_counter = 0
while True:
    answer_state = (screen.textinput(title=f"{state_counter}/50 guessed", prompt="What's another state's name?")).title()
    if answer_state == "Exit":
        break
    elif state_counter == 50:
        break
    else:
        if answer_state in states:
            state_counter += 1
            states.remove(answer_state)
            write_a_state(answer_state)

#states_to_learn.csv
forgotten_states = {
    "states": states,
}

new_data = pandas.DataFrame(forgotten_states)
new_data.to_csv("states_to_learn.csv")
print(new_data)



#its gonna keep our screen on, even after the program ends
turtle.mainloop()


