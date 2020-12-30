import time
from turtle import Turtle, Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

GAME_IS_ON = True
while GAME_IS_ON:
    time.sleep(0.1)
    screen.update()

    scoreboard.display_score()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            GAME_IS_ON = False

    # Detect when player reaches the other side
    if player.distance(player.finish_line) < 1:
        scoreboard.add_point()
        player.goto(player.starting_position)
        car_manager.level_up()

screen.exitonclick()
