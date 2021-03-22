import turtle
from turtle import*
import sys

font2 = "Midnight-minutes"


#screen for output
screen = turtle.Screen()
screen.setup(width = 1364 , height = 720)
# Defining a turtle Instance
t = turtle.Turtle()
t.speed(1)


turtle.shape("circle")
# initially penup()
t.penup()
t.goto(-400, 250)
t.pendown()


# Orange Rectangle 
#white rectangle
t.color("orange")
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(167)
t.right(90)
t.forward(800)
t.end_fill()
t.left(90)
t.color("white")
t.forward(167)
 
# Green Rectangle
t.color("green")
t.begin_fill()
t.forward(167)
t.left(90)
t.forward(800)
t.left(90)
t.forward(167)
t.end_fill()
 
# Big Blue Circle
t.penup()
t.goto(70, 0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(70)
t.end_fill()
 
# Big White Circle
t.penup()
t.goto(60, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(60)
t.end_fill()
 
# Mini Blue Circles
t.speed(11)
t.penup()
t.goto(-57, -8)
t.pendown()
t.color("navy")
for i in range(24):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
    t.forward(15)
    t.right(15)
    t.pendown()
     
# Small Blue Circle
t.penup()
t.goto(20, 0)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()
# Spokes
t.speed(1)
t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(2)
for i in range(24):
    t.forward(60)
    t.backward(60)
    t.left(15)

t.penup()
t.goto(-400, 250)
t.pendown()
t.color("black")
t.right(90)
t.speed(20)
t.forward(800)
t.right(90)
t.forward(167*3)
t.right(90)
t.forward(800)
t.right(90)
t.forward(167*3)


t.penup()
t.goto(-400, -300)
t.pendown()
t.write("SUBSCRIBE TO MY YOUTUBE CHANNEL-       /LAZY PROGRAMMERS(link in the description)", font=(font2,15, "normal"))

turtle.color("navy")
t.penup()
t.goto(-10,-290)
t.pendown()
t.color("red")
t.hideturtle()
t.setheading(90)
t.begin_fill()
t.fillcolor("red")
for i in range(2):
    t.forward(10)
    t.circle(-10,90)
    t.fd(15)
    t.circle(-10,90)
t.end_fill()
t.up()
t.goto(1,-289)
t.down()
t.color("white")
t.begin_fill()
t.fillcolor("white")
for i in range(3):
    t.fd(10)
    t.right(120)
t.end_fill()

t.color("black")
t.penup()
t.goto(-280, -320)
t.pendown()
t.write("Follow me on instagram - @sarb.theiitain.6542", font=(font2,15, "normal"))

t.penup()
t.goto(-320, 280)
t.pendown()
t.write("MADE BY SARBJEET", font=(font2,50, "normal"), move=True)


     
#to hold the 
#output window
turtle.done()
