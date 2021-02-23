from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0] ## To head first segment object

    def create_snake(self):
        starting_x_position = 0

        for _ in range(3):
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.goto(x=starting_x_position, y=0)
            self.snakes.append(segment)
            starting_x_position -= 20

    def move(self):
        for snake_number in range(len(self.snakes) - 1, 0, -1):  # reverse for

            self.snakes[snake_number].goto(
                x=self.snakes[snake_number - 1].xcor(),
                y=self.snakes[snake_number - 1].ycor()
            )
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
