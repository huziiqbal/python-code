from turtle import Turtle, Screen
import random
huzi1 = Turtle()
huzi1.shape("turtle")
huzi1.color("pale violet red")
huzi1.penup()
huzi1.goto(-300, 0)
huzi1.pendown()

huzi2 = Turtle()
huzi2.shape("turtle")
huzi2.color("green")
huzi2.penup()
huzi2.goto(-300, 30)
huzi2.pendown()

huzi3 = Turtle()
huzi3.shape("turtle")
huzi3.color("brown")
huzi3.penup()
huzi3.goto(-300, 60)
huzi3.pendown()

huzi4 = Turtle()
huzi4.shape("turtle")
huzi4.color("red")
huzi4.penup()
huzi4.goto(-300, 90)
huzi4.pendown()


for i in range (100):
    step = random.randint(0,10)
    huzi1.forward(step)

    step2 = random.randint(0,10)
    huzi2.forward(step2)

    step3 = random.randint(0,10)
    huzi3.forward(step3)

    step4 = random.randint(0,10)
    huzi4.forward(step4)


screen = Screen()
screen.exitonclick()
