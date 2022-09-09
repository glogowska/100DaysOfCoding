import turtle as t
import random
# import colorgram
#
#
# def get_color(color_palet, size):
#     new_list = []
#     for color in range (0, size):
#         rgb = color_palet[color].rgb
#         color_tuple = (rgb[0], rgb[1], rgb[2])
#         new_list.append(color_tuple)
#     return new_list
#
#
# colors = colorgram.extract("image.jpg", 30)
# colors_list = get_color(colors, 30)

t.colormode(255)
created_colors = [(233, 233, 232), (230, 232, 237), (225, 233, 228), (236, 231, 233), (207, 158, 82), (54, 89, 130), (144, 91, 40), (139, 27, 50), (221, 207, 105), (132, 177, 202), (157, 47, 83), (45, 55, 104), (169, 160, 40), (130, 189, 143), (83, 20, 44), (38, 43, 65), (186, 93, 107), (186, 140, 171), (86, 118, 179), (58, 39, 32), (89, 156, 93), (79, 153, 164), (195, 80, 72), (79, 74, 44), (45, 74, 77), (59, 128, 120), (162, 202, 216), (44, 76, 76), (220, 175, 186), (178, 188, 213)]


def draw_dot(radius):
    turtle.dot(radius, random.choice(created_colors))


def set_position(x,y):
    turtle.setx(x)
    turtle.sety(y)


def million_dollar_picture(dot_size, step, rows, cols):
    for row in range(rows):
        for col in range(cols):
            turtle.pendown()
            draw_dot(dot_size)
            turtle.penup()
            turtle.forward(step)
        global y
        y += 50
        set_position(x, y)


turtle = t.Turtle()
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
x = -300
y = -300
set_position(x, y)


million_dollar_picture(20, 50, 10, 10)





screen = t.Screen()
screen.exitonclick()






