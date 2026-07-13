from turtle import Turtle , Screen
from snake import Snake
from Snake_Game_Food import Food
from Snake_Game_Score import Score

import time

pencil = Turtle()
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()

score = Score()



screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.turn_right,"Right")
screen.onkey(snake.turn_left,"Left")


def inc_size():
        new_segment = Turtle()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.penup()#line 
        snake.snake.append(new_segment)
game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake[0].distance(food) < 15:
        food.collision()
        inc_size()
        score.scoreboard()
    if snake.snake[0].xcor() < -380 or snake.snake[0].xcor() > 380 or snake.snake[0].ycor() < -380 or snake.snake[0].ycor() > 380:
        pencil.goto(-50,0)
        pencil.color("white")
        pencil.write(f"Game Over" ,
            font=("Arial", 18, "bold"))
        break





screen.exitonclick()

