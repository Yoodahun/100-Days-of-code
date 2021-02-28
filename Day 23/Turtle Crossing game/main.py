import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

the_turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(the_turtle.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    #Detect collision car
    for car in car_manager.all_cars:
        if car.distance(the_turtle) < 20:
            game_is_on = False
            scoreboard.game_over()
            break

    #Detect successful crossing
    if the_turtle.check_finish_line():
        the_turtle.position_clear()
        scoreboard.increase_level()
        car_manager.level_speed_up()

screen.exitonclick()
