# -------------------- Importing stuff and setting the tone -------------------- #

'''

PATCH NOTES (VERSION 2):

- Changed cube generation method

COLOR CHANGES:
    - Removed "random noise" color
    - Put a more coherent (albeit still random) grayscale
    - Added a "shadow gradient" effect
    
- Graph looks less like ass and a bit more 3d

- Made "bounds" and "dots per layer" user generated

'''

import turtle
import random
turtle.colormode(255)
turtle.Screen().bgcolor((40,40,40))
turtle.hideturtle()

# -------------------- Defining functions and variables -------------------- #

cBound = 100

dpl = turtle.numinput("","dots per layer (around 200 recommended)")
dpl = int(dpl)

bounds = int(dpl/6)

xCoord, yCoord = 0, 0
cValue = 0
depth = bounds/4

def teleport(t):
    """teleports pen to a random location with a random color"""
    
    xCoord, yCoord = random.randint(-bounds,bounds) , random.randint(-bounds,bounds)
    cValue = random.randint(60+cIncrement,cBound)
    depth = bounds/5
   
    t.up()
            
    t.goto(xCoord + zshift + xshift ,yCoord + zshift + yshift)
    t.down()
    t.color((cValue,cValue,cValue))
    t.dot(depth)
    
def graph(t):
    """ Draws a 3-d graph"""
    
    t.width(1)
    
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

    t.width(2)
    t.up()
    t.goto(0,-500)
    t.left(90)
    t.down()
    t.forward(1000)
    t.left(-90)
    t.width(1)
    
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
t.speed(100)

locations = set()

xshift = 0
yshift = 0
zshift = 0

cIncrement = 0

# -------------------- Program -------------------- #

graph(t)

for i in range(4):
    for i in range(dpl): # (is done n times) teleports pen to random location w random color while making sure pen can't tp to the same location twice (uses an array of past locations)
        
        teleport(t)
        
        if ((xCoord,yCoord) in locations):
            while ((xCoord,yCoord) in locations):
                xCoord, yCoord = random.randint(-bounds,bounds), random.randint(-bounds,bounds)
        else:
            locations.add((xCoord,yCoord))
            print((xCoord,yCoord))   
    if cBound <= 254:
        cBound += 50
    elif cIncrement <= 254:
        cIncrement += 10
    else:
        continue
    depth += 10
    zshift += -bounds/4
    print(locations)
    

    
t.up() #resets to center
t.goto(0,0)

turtle.exitonclick()