from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def one_cycle(self):
        cyc = random.randint(1,2)
        if cyc == 1 :
            randomx = random.randint(0,350)
            randomy = random.randint(0,250)
            x = randomx + x
            y = randomy + y
            while ( x < 350 or y < 250):
                    self.goto(x , y)
                    self.goto(0 , -250)

        if cyc == 2 :
            randomx = random.randint(0,350)
            randomy = random.randint(0,-250)
            x = randomx + x
            y = randomy - y
            while ( x < 350 or y < 250):
                    self.goto(x , y)
                    self.goto(0 , -250)








        # self.goto(0,-250)
        # time.sleep(0.01)
        # self.goto(350,random1)
        # time.sleep(0.01)
        # self.goto(0,-250)
        # time.sleep(0.01)
        # self.goto(-350,random2)
        # time.sleep(0.01)
        # self.goto(0,-250)
        # time.sleep(0.01)



