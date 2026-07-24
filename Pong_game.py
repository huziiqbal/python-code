from turtle import Screen,Turtle
from pong_game_paddle import Paddle
from Pong_game_ball import Ball
import time
screen =  Screen()

ball = Ball()
paddle1 = Paddle()
paddle2 = Paddle()

screen.bgcolor("black")
screen.screensize(800,600)
screen.title("Pong Game")

screen.tracer(0)

paddle1.goto(330,0)
paddle2.goto(-330,0)


screen.listen()
screen.onkeypress(paddle1.go_up,"Up")
screen.onkeypress(paddle1.go_down,"Down")

screen.onkeypress(paddle2.go_up,"w")
screen.onkeypress(paddle2.go_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(0.07)
    screen.update()
    ball.move()
    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.bounce()
    if ball.distance(paddle1) < 50 or ball.distance(paddle2) < 50:
        ball.reverse()


screen.exitonclick()

