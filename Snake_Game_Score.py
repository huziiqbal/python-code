from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pen = Turtle()
        self.pen2 = Turtle()
        self.score = 0
        with open("Snake_Game_Data.txt", "r") as k :
            self.highest_score  = int (k.read())

        self.scoreboard()

    def scoreboard(self):
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(170, 360)
        self.pen.color("white")
        self.pen.clear()

        self.pen2.penup()
        self.pen2.hideturtle()
        self.pen2.goto(170, 300)
        self.pen2.color("white")
        self.pen2.clear()

        self.pen.write(f"Score: {self.score}",
                font=("Arial", 18, "bold"))
        self.score +=1
        if (self.score > self.highest_score):
            self.highest_score = self.score - 1
            with open("Snake_Game_Data.txt", "w") as f :
                f.write(f"{self.highest_score}")

        self.pen2.write(f"Highest Score: {self.highest_score}",
                font=("Arial", 18, "bold"))





