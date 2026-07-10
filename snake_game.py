from turtle import Screen,Turtle
from snake import Snake
from Snake_Game_Food import Food
import time
screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()




screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.turn_right,"Right")
screen.onkey(snake.turn_left,"Left")


game = True
score = 0
pen = Turtle()
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake[0].distance(food) < 15:
        food.collision()
        score +=1
        pen.penup()
        pen.hideturtle()
        pen.goto(290, 260)
        pen.color("white")
        pen.clear()
        pen.write(f"{score}",
                font=("Arial", 18, "bold"))




screen.exitonclick()

