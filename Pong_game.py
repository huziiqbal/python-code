from turtle import Screen,Turtle
from pong_game_paddle import Paddle
from Pong_game_ball import Ball
from Pong_game_scoreboard import Score
import time
screen =  Screen()
score = Score()
ball = Ball()
paddle1 = Paddle()
paddle2 = Paddle()

screen.bgcolor("black")
screen.screensize(800,600)
screen.title("Pong Game")

screen.tracer(0)


pencil = Turtle()
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
    if ball.distance(paddle1) < 50 and ball.xcor() > 310:
        ball.reverse()
        score.scoreboard1()
    if ball.distance(paddle2) < 50 and ball.xcor() < -310:
        ball.reverse()
        score.scoreboard2()
    if ball.xcor() > 340 or ball.xcor() < -340 or ball.ycor() > 270 or ball.ycor() < -270 :
        pencil.goto(-50,0)
        pencil.color("white")
        pencil.write(f"Game Over" ,
            font=("Arial", 18, "bold"))
        break


screen.exitonclick()

