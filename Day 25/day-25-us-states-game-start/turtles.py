from turtle import Turtle


class Turtler(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def name(self, user, x, y):
        self.write(f"{user}", True, align="center")
        self.goto(x, y)



