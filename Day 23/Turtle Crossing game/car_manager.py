from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.max_create_number = 6

    def create_cars(self):
        random_chance = random.randint(1, self.max_create_number)

        if random_chance == 1: # when 1, create cars
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            # new_car.setheading(180)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(x=300, y=random.randint(-240, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)


    def level_speed_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        self.max_create_number -= 1

