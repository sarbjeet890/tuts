import turtle
from turtle import*
import sys

font2 = "Midnight-minutes"


#screen for output
screen = turtle.Screen()
# Defining a turtle Instance
t = turtle.Turtle()
t.speed(50)
t.fillcolor("black")
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
t.goto(-300, -300)
t.pendown()
t.write("SUBSCRIBE TO MY YOUTUBE CHANNEL LAZY PROGRAMMERS", font=(font2,15, "normal"))

t.penup()
t.goto(-300, -320)
t.pendown()
t.write("Follow me on instagram - @sarb.theiitain.6542", font=(font2,15, "normal"))

t.penup()
t.goto(-320, 280)
t.pendown()
t.write("MADE BY SARBJEET", font=(font2,50, "normal"), move=True)


     
#to hold the 
#output window
turtle.done()