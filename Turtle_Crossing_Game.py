from turtle import Screen,Turtle
import random
import time
from Scoreboard_Turtle_Race_Game import Scoreboard

screen = Screen()
score = Scoreboard()
screen.bgcolor("light cyan")
screen.setup(width=600, height=600)

turtles= []
Player = Turtle()
Player = Turtle()
Pen = Turtle()
Pen.penup()
Pen.goto(0,0)
Pen.color("black")
Pen.hideturtle()


def move():
    Player.forward(20)

screen.listen()
screen.onkey(move,"Up")


Player.shape("turtle")
Player.color("pale violet red","firebrick")
Player.penup()
Player.left(90)
Player.goto(0,-220)



for y in range (10):
    screen.tracer(0)
    for u in range (200):
        huzi = Turtle()
        huzi.shape("square")
        huzi.color("black")
        huzi.penup()
        huzi.goto(-300 - (y * 150), -180 + u * 80)
        huzi.pendown()
        turtles.append(huzi)





game_over = False
for u in range (10):
    for i in range (len(turtles)):
        step = random.randint(0,10)
        turtles[i].penup()
        turtles[i].forward(step * 5)

        if Player.distance(turtles[i]) < 20:
            Pen.write(f"Game Over" , font=("Arial", 18, "bold"))
            game_over = True
            break
    if game_over:
        break
    screen.update()
    time.sleep(0.3)




screen.exitonclick()
