from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_cor = 10
        self.x_cor = 10

    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)
    def bounce(self):
        self.y_cor *= -1
    def reverse(self):
        self.x_cor *= -1





# class Ball(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.color("white")
#         self.penup()
#         self.goto(0 , -250)
#         self.x = random.randint(0, 50)
#         self.y = random.randint(-250, -200)
#         self.goto(self.x, self.y)
#         self.direction = "left"

#     def move_left(self):
#             self.goto(self.x, self.y)
#             self.x -= 10
#             self.y += 10
#             if self.x > -350 and -250 < self.y < 250:
#                 self.direction = "right"
#                 self.x = 0
#                 self.y = -250


#     def move_right(self):
#             self.goto(self.x, self.y)
#             self.x += 10
#             self.y += 10
#             if self.x < 350 and -250 <= self.y < 250:
#                 self.direction = "left"
#                 self.x = random.randint(0, 50)
#                 self.y = random.randint(-250, -200)


