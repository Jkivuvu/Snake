import turtle
import time

SNAKE = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):

        self.snakes = []
        self.create_snake()

    def create_snake(self):

        for positions in SNAKE:
            self.add_segment(positions)

    def add_segment(self, positions):
        snake1 = turtle.Turtle()
        snake1.penup()
        snake1.shape("square")
        snake1.color("white")
        snake1.goto(positions)
        self.snakes.append(snake1)

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def move(self):

        for snake2 in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake2 - 1].xcor()
            new_y = self.snakes[snake2 - 1].ycor()
            self.snakes[snake2].goto(new_x, new_y)
        self.snakes[0].forward(MOVE_DISTANCE)

    def snake_reset(self):
        for S in self.snakes:
            S.goto(-900, -900)

        self.snakes.clear()
        self.create_snake()

    def up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)

    def Right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)

    def Left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)

    def Down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)
