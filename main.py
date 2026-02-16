import turtle
import random
from turtle import Turtle, Screen
from hit_wall import Hit_Ball
screen = Screen()

player1 = Turtle()
player2 = Turtle()
ball = Turtle()
tim = Turtle()

check = Hit_Ball(ball)


screen.setup(1000,640)
screen.bgcolor("black")

screen.tracer(0)

tim.speed("fastest")
tim.penup()
tim.color("white")
tim.goto(0,-320)
tim.setheading(90)

while tim.ycor()<630:
    tim.penup()
    tim.forward(20)
    tim.pendown()
    tim.forward(20)
tim.hideturtle()





player1.penup()
player1.color("white")
player1.shape("square")
player1.goto(-490,0)
player1.shapesize(6,1)


player2.penup()
player2.color("white")
player2.shape("square")
player2.goto(480,0)
player2.shapesize(6,1)

ball.shape("circle")
ball.color("white")
ball.penup()
ball.shapesize(1.6)

screen.tracer(1)

screen.listen()









ball.speed("fastest")
ball.setheading(random.randint(0,360))

def game():
    ball.forward(10)
    check.is_hitting_to_wall()
    check.is_hitting_to_players(player1,player2)
    screen.ontimer(game,1)
game()














turtle.mainloop()