#Turtle Maze Challenge - www.101computing.net/turtle-maze/
import turtle
import maze

myPen=turtle.Turtle()
myPen.penup()
myPen.goto(20,-180)
myPen.pendown()
myPen.shape('turtle')
myPen.color("#DB148E")
myPen.width(5)
myPen.left(90)

"""
-----.-----
-.........-
--.-----.--
-.........-
-----.-----

"""



#Start of maze
myPen.forward(70)

myPen.right(90)
myPen.forward(120)

myPen.left(90)
myPen.forward(60)

myPen.left(90)
myPen.forward(120)

myPen.right(90)



#Width from (0,0) = 300
#Height from Start to Finish = 400
#Height of one box = 130
#Height to first line = 70

input()





