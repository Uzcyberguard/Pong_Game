from turtle import Turtle, Screen
screen = Screen()

player1 = Turtle()
player2 = Turtle()
ball = Turtle()
tim = Turtle()

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

is_on = True
while is_on:
    ball.forward(6)
















screen.exitonclick()