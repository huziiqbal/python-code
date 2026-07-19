from turtle import Screen,Turtle
from pong_game_paddle import Paddle
from Pong_game_ball import Ball
screen =  Screen()

ball = Ball()
paddle1 = Paddle()
paddle2 = Paddle()

screen.bgcolor("black")
screen.screensize(800,600)
screen.title("Pong Game")



paddle1.goto(350,0)
paddle2.goto(-350,0)


screen.listen()
screen.onkeypress(paddle1.start_up,"Up")
screen.onkeyrelease(paddle1.start_down,"Up")
screen.onkeypress(paddle1.stop_up,"Down")
screen.onkeyrelease(paddle1.stop_down,"Down")

screen.onkeypress(paddle2.start_up,"w")
screen.onkeyrelease(paddle2.start_down,"w")
screen.onkeypress(paddle2.stop_up,"s")
screen.onkeyrelease(paddle2.stop_down,"s")


game_is_on = True
while game_is_on:
    screen.update()
    paddle1.move()
    paddle2.move()
    ball.one_cycle()



screen.exitonclick()

