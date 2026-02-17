from turtle import Turtle
class Score():
    def __init__(self):
        self.sc = Turtle()
    def write(self):
        self.sc.penup()
        self.sc.goto(-150,280)
        self.sc.color("red")

        self.sc.write("❤️❤️❤️❤️❤️",align="center",font=("Arial",18,"bold"))
