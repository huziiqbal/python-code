from turtle import Screen,Turtle
import random
import time

screen = Screen()

turtles= []
Player = Turtle()


def move():
    Player.forward(20)

screen.listen()
screen.onkey(move,"Up")


Player.shape("turtle")
Player.color("pale violet red","firebrick")
Player.penup()
Player.left(90)
Player.goto(0,-200)

for y in range (10):
    screen.tracer(0)
    for u in range (10):
        huzi = Turtle()
        huzi.shape("square")
        huzi.shapesize(stretch_wid=1,stretch_len=1.5)
        huzi.color("black")
        huzi.penup()
        huzi.goto(-300,-200 + u* 70 )
        huzi.pendown()

        turtles.append(huzi)


    for u in range (10):
        for i in range (len(turtles)):
            step = random.randint(0,10)
            turtles[i].penup()
            turtles[i].forward(step * 5)
        screen.update()
        time.sleep(0.2)



screen.exitonclick()
