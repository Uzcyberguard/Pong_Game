from turtle import Turtle
import time,random
class Score():
    def __init__(self,ball):
        self.sc = Turtle()
        self.live = 5
        self.b = ball
    def write(self):
        self.sc.penup()
        self.sc.goto(0,280)
        self.sc.color("red")

        self.sc.write("❤"*self.live,align="center",font=("Arial",18,"bold"))
        self.sc.hideturtle()
    def checking(self):
        if self.b.xcor()> 520 or self.b.xcor()<-520:
            self.sc.clear()
            self.live -=1
            self.sc.write("❤" * self.live+"💘"*(5-self.live), align="center", font=("Arial", 18, "bold"))
            time.sleep(1)
            self.b.goto(0,0)
            self.b.setheading(random.randint(-60,-20))