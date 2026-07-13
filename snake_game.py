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


game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake[0].distance(food) < 15:
        food.collision()
        score.scoreboard()
    if snake.snake[0].xcor() < -380 or snake.snake[0].xcor() > 380 or snake.snake[0].ycor() < -380 or snake.snake[0].ycor() > 380:
        pencil.goto(0,0)
        pencil.color("white")
        pencil.write(f"Game Over")
        break





screen.exitonclick()

