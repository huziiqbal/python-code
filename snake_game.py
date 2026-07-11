from turtle import Screen
from snake import Snake
from Snake_Game_Food import Food
from Snake_Game_Score import Score

import time
screen = Screen()
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
        score.score()






screen.exitonclick()

