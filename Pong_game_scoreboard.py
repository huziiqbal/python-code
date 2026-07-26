from turtle import  Turtle
class Score (Turtle ):
    def __init__(self):
        super().__init__()
        self.pen1 = Turtle()
        self.pen2 = Turtle()
        self.score1 = 0
        self.score2 = 0
        self.scoreboard1()
        self.scoreboard2()

    def scoreboard1(self):
        self.pen1.penup()
        self.pen1.hideturtle()
        self.pen1.goto(290,210 )
        self.pen1.color("white")
        self.pen1.clear()
        self.pen1.write(f"{self.score1}",
                        font=("Arial", 18, "bold"))
        self.score1 +=1
    def scoreboard2(self):
        self.pen2.penup()
        self.pen2.hideturtle()
        self.pen2.goto(-290,210 )
        self.pen2.color("white")
        self.pen2.clear()
        self.pen2.write(f"{self.score2}",
                        font=("Arial", 18, "bold"))
        self.score2 +=1

