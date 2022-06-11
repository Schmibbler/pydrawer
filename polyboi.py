import turtle
import math
import random

turtle.colormode(255)
screenSize = 800
poly = 7
sideLength = 10
turtle.speed(0)
turtle.setup(screenSize, screenSize) 

turtleTurns = 0
polyAmount = 0
lineCount = 0

turn = 180 - (((poly - 2) * 180)/poly)
pi = 3.1415
a = sideLength*(math.cos((pi/180)*(360/poly)))
print(a)
fullLen = sideLength + 2*a
polyPerLine = round((screenSize/fullLen), 0)
polyPerLines = polyPerLine
print(polyPerLine)

turtleShape = ['arrow', 'circle', 'square', 'triangle', 'turtle', 'classic']

turtle.up()
turtle.setx(-.5*(screenSize) + a)
turtle.sety((0.5)*screenSize)
turtle.down()

while lineCount < polyPerLine:
    while polyAmount < polyPerLines:
        turtleInt = random.randint(0, 5)
        turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        turtle.pensize(3)
        turtle.shape(turtleShape[turtleInt])
        while turtleTurns < poly:
            turtle.forward(sideLength)
            turtle.right(turn)
            turtleTurns += 1
        else:
            turtleTurns = 0
        turtle.up()
        turtle.forward(fullLen)
        turtle.down()
        polyAmount += 1
    else:
        polyAmount = 0
        turtle.up()
        y = int(turtle.ycor())
        turtle.sety(y - fullLen)
        x = int(turtle.xcor())
        turtle.setx(x - (fullLen * polyPerLine))
        turtle.down()   
    lineCount += 1
       
        
        
turtle.exitonclick()
turtle.bye()



