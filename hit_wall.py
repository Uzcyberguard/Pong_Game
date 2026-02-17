from turtle import Turtle
class Hit_Ball:
    def __init__(self,ball):

         self.ball = ball

    def is_hitting_to_wall(self):
        if self.ball.ycor()>=300 or self.ball.ycor()<=-290:

            self.ball.setheading(-self.ball.heading())
            self.ball.forward(10)
    def is_hitting_to_players(self,player1,player2):
        if (self.ball.xcor()>=460 or self.ball.xcor()<=-470) and (self.ball.distance(player1) <= 66.2 or self.ball.distance(player2) <= 66.2):
            self.ball.setheading(180-self.ball.heading())
            self.ball.forward(10)
