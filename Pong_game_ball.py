from turtle import Turtle
import random
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape ("circle")
        self.color ("white")
        self.penup()

    def one_cycle(self):
        random1 = random.randint(-250,250)
        random2 = random.randint(-250,250)
        self.goto(0,-250)
        time.sleep(0.5)
        self.goto(350,random1)
        time.sleep(0.5)
        self.goto(0,-250)
        time.sleep(0.5)
        self.goto(-350,random2)
        time.sleep(0.5)
        self.goto(0,-250)
        time.sleep(0.5)



