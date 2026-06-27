from turtle import Turtle, Screen
huzi = Turtle()
huzi.shape("turtle")
huzi.color("pale violet red","firebrick")
huzi.pensize(5)
huzi.speed(4)
huzi.penup()
huzi.goto(-300, 0)
huzi.pendown()

def right_run():
    huzi.forward(100)
    huzi.right(90)


def move(dis):
    huzi.penup()
    huzi.forward(dis)
    huzi.pendown()


def down(dis):
    huzi.right(90)
    huzi.forward(dis)


def up(distance):
    huzi.backward(distance)


huzi.right(90)
huzi.forward(150)
huzi.penup()
huzi.backward(50)
huzi.pendown()
huzi.left(90)
right_run()
huzi.forward(50)
huzi.backward(150)
huzi.forward(150)

huzi.penup()
huzi.left(135)
huzi.forward(100)
huzi.pendown()
huzi.right(135)
huzi.forward(70)
huzi.left(90)
huzi.forward(50)
huzi.left(90)
huzi.forward(70)
huzi.penup()
huzi.right(90)
huzi.forward(30)
huzi.pendown()
huzi.forward(100)
huzi.right(135)
huzi.forward(100)
huzi.left(135)
huzi.forward(80)
huzi.penup()
huzi.forward(30)
huzi.left(90)
huzi.pendown()
huzi.forward(80)
huzi.penup()
huzi.forward(30)
huzi.dot(20)
huzi.penup()
huzi.forward(30)



screen = Screen()
screen.exitonclick()


# from turtle import Turtle, Screen
# kavya = Turtle()
# kavya.shape("turtle")
# kavya.color("pale violet red","firebrick")
# kavya.pensize(5)
# kavya.speed(4)
# kavya.penup()
# kavya.goto(-300, 0)
# kavya.pendown()


# kavya.right(90)
# kavya.forward(100)
# kavya.penup()
# kavya.backward(50)
# kavya.pendown()
# kavya.left(135)
# kavya.forward(70)
# kavya.backward(70)
# kavya.right(90)
# kavya.forward(70)
# kavya.left(45)
# kavya.penup()
# kavya.forward(30)
# kavya.pendown()



# kavya.left(65)
# kavya.forward(100)
# kavya.right(135)
# kavya.forward(100)
# kavya.backward(50)
# kavya.right(110)
# kavya.forward(35)
# kavya.penup()
# kavya.left(90)
# kavya.forward(50)
# kavya.left(90)
# kavya.forward(100)
# kavya.pendown()


# kavya.left(65)
# kavya.forward(90)
# kavya.backward(90)
# kavya.left(50)
# kavya.forward(90)
# kavya.backward(90)
# kavya.right(115)
# kavya.penup()
# kavya.forward(90)
# kavya.pendown()



# kavya.left(90)
# kavya.forward(50)
# kavya.left(45)
# kavya.forward(50)
# kavya.backward(50)
# kavya.right(90)
# kavya.forward(50)
# kavya.backward(50)
# kavya.right(135)
# kavya.forward(50)
# kavya.left(90)
# kavya.penup()
# kavya.forward(80)
# kavya.pendown()

# kavya.left(65)
# kavya.forward(100)
# kavya.right(135)
# kavya.forward(100)
# kavya.backward(50)
# kavya.right(110)
# kavya.forward(35)
# kavya.penup()
# kavya.left(90)
# kavya.forward(50)
# kavya.left(90)
# kavya.forward(100)
# kavya.pendown()

# screen = Screen()
# screen.exitonclick()
