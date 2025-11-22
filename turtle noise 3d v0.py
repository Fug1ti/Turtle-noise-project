# -------------------- Importing stuff and setting the tone -------------------- #

import turtle
import random
turtle.colormode(255)
turtle.Screen().bgcolor((50,50,50))

# -------------------- Defining functions and variables -------------------- #

xCoord, yCoord = random.randint(-250,250), random.randint(-250,250)

rValue, gValue, bValue = random.randint(0,255), random.randint(0,255), random.randint(0,255)

def teleport(t): # teleports pen to a random location with a random color
    t.up()
    t.goto(xCoord,yCoord)
    t.down()
    t.color((rValue,gValue,bValue))
    t.dot(10)
    
def graph(): # draws a graph
    
    t.width(3)
    
    t.up()
    t.goto(-500,0)
    t.down()
    t.forward(1000)
    
    t.up()
    t.goto(0,-500)
    t.left(90)
    t.down()
    t.forward(1000)
    
    t.up
    t.goto(0,0)
    t.left(-90)
    
t = turtle.Pen()
t.speed(10)

locations = []

n = turtle.numinput("","How many dots would you like to draw?")
n = int(n)

# -------------------- Program -------------------- #

graph()

for i in range(n): # (is done n times) teleports pen to random location w random color while making sure pen can't tp to the same location twice (uses an array of past locations)
    
    teleport(t)
    xCoord, yCoord = random.randint(-250,250), random.randint(-250,250)
    rValue, gValue, bValue = random.randint(0,255), random.randint(0,255), random.randint(0,255)
    
    if [xCoord,yCoord] in locations:
        while [xCoord,yCoord] in locations:
            xCoord, yCoord = random.randint(-250,250), random.randint(-250,250)
    else:
        locations.append([xCoord,yCoord])
t.up()
t.goto(0,0)

turtle.exitonclick()