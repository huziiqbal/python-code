from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pen = Turtle()
        self.score = 0
        self.scoreboard()

    def scoreboard(self):
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(290, 260)
        self.pen.color("white")
        self.pen.clear()
        self.pen.write(f"{self.score}",
                font=("Arial", 18, "bold"))
        self.score +=1


