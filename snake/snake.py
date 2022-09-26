from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
x = 0.00
y = 0.00

class Snake:

    def __init__(self):
        self.num_of_blocks = 3
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

    def create_snake(self):
        global x
        global y
        for block in range(0, 3):
            self.add_block(x, y)
            # self.blocks.append(Turtle(shape="square"))
            # self.blocks[block].penup()
            # self.blocks[block].color("white")
            # self.blocks[block].goto(x, y)
            x -= 20

    def add_block(self, position_x, position_y):
        self.blocks.append(Turtle(shape="square"))
        self.blocks[-1].penup()
        self.blocks[-1].color("white")
        self.blocks[-1].speed("fastest")
        self.blocks[-1].goto(position_x, position_y)

    def extend(self):
        self.add_block(self.blocks[-1].xcor(), self.blocks[-1].ycor())

    def move(self):
        for blo_num in range(len(self.blocks) - 1, 0, -1):
            new_x = self.blocks[blo_num - 1].xcor()
            new_y = self.blocks[blo_num - 1].ycor()
            self.blocks[blo_num].goto(new_x, new_y)
        self.blocks[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):
        for blo in self.blocks:
            blo.goto(10000, 10000)
        self.blocks.clear()
        self.create_snake()
        self.head = self.blocks[0]