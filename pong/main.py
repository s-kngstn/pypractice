import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((360, 0))
left_paddle = Paddle((-360, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

GAME_IS_ON = True
while GAME_IS_ON:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 335 or ball.distance(
            left_paddle) < 50 and ball.xcor() < -335:
        ball.bounce_x()

    # Detect when right paddles miss and ball has gone out of bounds
    if ball.distance(right_paddle) > 50 and ball.xcor() > 380:
        scoreboard.left_point()
        ball.reset_ball()
        screen.update()
        time.sleep(2.0)

    # Detect when left paddles miss and ball has gone out of bounds
    if ball.distance(left_paddle) > 50 and ball.xcor() < -380:
        scoreboard.right_point()
        ball.reset_ball()
        screen.update()
        time.sleep(2.0)
screen.exitonclick()
