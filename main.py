import turtle
import random
from turtle import Turtle, Screen
from hit_wall import Hit_Ball
from players_moving import Players_Moving
from score import Score


screen = Screen()
screen.title("Pong Game")
SPEED = 9
player1 = Turtle()
player2 = Turtle()
ball = Turtle()
tim = Turtle()

check = Hit_Ball(ball)
score = Score(Turtle)
score.write()
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
goo_up = False
goo_down = False
def tr():
    global goo_up
    goo_up = True
def tp():
    global goo_up
    goo_up = False
def rt():
    global goo_down
    goo_down = True
def rp():
    global goo_down
    goo_down = False
header = Players_Moving(player1,player2)
screen.listen()
screen.onkeypress(fun = tr,key = "Up")
screen.onkeyrelease(fun = tp,key = "Up")
screen.onkeypress(fun = rt,key = "Down")
screen.onkeyrelease(fun = rp,key = "Down")





ball.speed("fastest")
ball.setheading(random.randint(-60,60))

def game():
    ball.forward(SPEED)
    if goo_up:
        header.p_up()
    if goo_down:
        header.p_down()
    check.is_hitting_to_wall()
    check.is_hitting_to_players(player1,player2)
    screen.ontimer(game,10)
game()














turtle.mainloop()