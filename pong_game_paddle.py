from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.moving_up = False
        self.moving_down = False


    def go_up(self):
            new_ycor = self.ycor() + 30
            self.goto(self.xcor() , new_ycor)
    def go_down(self):
        new_ycor = self.ycor() -  30
        self.goto(self.xcor() , new_ycor)











    # def start_up(self):
    #     self.moving_up = True

    # def stop_up(self):
    #     self.moving_up = False

    # def start_down(self):
    #     self.moving_down = True

    # def stop_down(self):
    #     self.moving_down = False


    # def move(self):
    #     if self.moving_up:
    #         self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    #     if self.moving_down:
    #         self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)



