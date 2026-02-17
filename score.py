from turtle import Turtle
class Score():
    def __init__(self,ball):
        self.sc = Turtle()
        self.live = 3
        self.b = ball
    def write(self):
        self.sc.penup()
        self.sc.goto(0,280)
        self.sc.color("red")

        self.sc.write("❤"*self.live,align="center",font=("Arial",18,"bold"))
        self.sc.hideturtle()
    def checking(self,ball):
        if self.b.xcor()> 510 or self.b.xcor<-510:
            self.live -=1
            self.sc.write("❤" * self.live+"💘"*(3-self.live), align="center", font=("Arial", 18, "bold"))