from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 3
        self.y_move = 3

    def move(self):
        ball_x_pos = self.xcor() + self.x_move
        ball_y_pos = self.ycor() + self.y_move
        self.goto(ball_x_pos, ball_y_pos)

    def bounce_y(self):
        self.y_move *= -1  # when collision occurred, multiply -1, so turn y position heading

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
