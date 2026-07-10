from turtle import Turtle

UP =90
DOWN = 270
LEFT  = 180
RIGHT = 0
class Snake :
    def __init__(self):
        self.pos = [(0,0), (-20,0),(-40,0)]
        self.snake = []
        self.create()
    def create(self):

        for i in self.pos:
            new_seg = Turtle()
            new_seg.shape("square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(i)
            self.snake.append(new_seg)

    def move(self):
            for k in range (len(self.snake) - 1, 0 , -1 ):
                new_x = self.snake[k - 1].xcor()
                new_y = self.snake[k - 1].ycor()
                self.snake[k].goto(new_x,new_y)
            self.snake[0].forward(20)
    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(270)

    def turn_left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(180)

    def turn_right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(0)





