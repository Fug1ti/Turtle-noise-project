# -------------------- Importing stuff and setting the tone -------------------- #

import turtle
import random
import math
turtle.colormode(255)
turtle.Screen().bgcolor((40,40,40))

bounds = 250

# -------------------- Defining functions and variables -------------------- #
xCoord, yCoord = 0, 0
rValue, gValue, bValue = 0, 0, 0
depth = 1

def teleport(t):
    """teleports pen to a random location with a random color"""
    
    xCoord, yCoord = random.randint(-bounds,bounds), random.randint(-bounds,bounds)
    rValue, gValue, bValue = random.randint(0,255), random.randint(0,255), random.randint(0,255)
    depth = 20
    
    if xCoord + yCoord >= bounds:
        depth = random.randint(5,12)
    else:
        depth = random.randint(10,20)
    
    t.up()
    
    if abs(yCoord + xCoord) >= 2*bounds or abs(yCoord - xCoord) >= 1.5*bounds: # kinda rotates the square...? lol. i'll analyse exactly how it works later
        while abs(yCoord + xCoord) >= 2*bounds or abs(yCoord - xCoord) >= 1.5*bounds:
            xCoord, yCoord = random.randint(-bounds,bounds), random.randint(-bounds,bounds)
            
    t.goto(xCoord,yCoord)
    t.down()
    t.color((rValue,gValue,bValue))
    t.dot(depth)
    
def graph(t):
    """ Draws a 3-d graph"""
    
    t.width(1)
    
    x = -400
    y = -400
    z = 500
    increment = 500
    t.color("green")
    
    for i in range(10):
        t.up()
        t.goto(-500,y)
        t.down()
        t.forward(1000)
        y += 100

    for i in range(10):
        t.up()
        t.goto(x,-500)
        t.left(90)
        t.down()
        t.forward(1000)
        t.left(-90)
        x += 100
    
    t.left(45)
    for i in range(20):
        t.up()
        t.goto(-500,z)
        t.down()
        t.forward(increment)
        increment += 500
        z -= 200
        
    t.left(-45)
    t.up()
    t.goto(-500,0)
    t.down()
    for i in range(-5,6):
        t.write(str(i),align="center", font=("Courier", 16, "bold"))
        t.forward(100)
        
    t.up()
    t.goto(0,-500)
    t.down()
    t.left(90)
    for i in range(-5,6):
        t.write(str(i),align="center", font=("Courier", 16, "bold"))
        t.forward(100)
        
    t.up()
    t.goto(-500,-500)
    t.down()
    t.left(-45)
    for i in range(-7,6):
        t.write(str(i),align="center", font=("Courier", 16, "bold"))
        t.forward(100)
        
    
    t.left(-90)
    

t = turtle.Pen()
t.speed(1000)

locations = []

n = turtle.numinput("","How many dots would you like to draw?")
n = int(n)

# -------------------- Program -------------------- #

graph(t)

for i in range(n): # (is done n times) teleports pen to random location w random color while making sure pen can't tp to the same location twice (uses an array of past locations)
    
    teleport(t)
    
    if ([xCoord,yCoord] in locations):
        while ([xCoord,yCoord] in locations):
            xCoord, yCoord = random.randint(-bounds,bounds), random.randint(-bounds,bounds)
    else:
        locations.append([xCoord,yCoord])
    
    print([xCoord, yCoord])
        
t.up() #resets to center
t.goto(0,0)

turtle.exitonclick()