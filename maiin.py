from turtle import Screen, Turtle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Gravity")
screen.tracer(0)

ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.04)
    screen.update()
    ball.move()
    if ball.ycor() < -280 or ball.ycor()>280:
        ball.bounce()
    if ball.xcor() <= -380 or ball.xcor() >= 380:
        ball.reflect()

screen.exitonclick()