"""
Given a maze string with . as valid nodes, and - as invalid nodes/walls, draw the maze
"""
import turtle
from turtle import Turtle
from Graph import MazeStringTo2DList

pixelDimensions = 600

# Functions as a C++ enum, assigns cardinal directions to numbers
Direction = {"NORTH":1, "EAST":2, "SOUTH":3, "WEST":4}


string = """-------.-------
-.............-
---.-------.---
-.............-
-------.-------
"""

maze = MazeStringTo2DList(string)
assert pixelDimensions % len(maze[0]) == 0
assert pixelDimensions % len(maze) == 0


# How long one character is
# Should I make the maze fixed length? (15x15 makes 40 wall length feasible)
wallWidth = pixelDimensions / len(maze[0])
wallHeight = wallWidth


# Turtle is about 600x600 pixels in size
# The origin for this is  (-300, 300), since (0, 0) is the center
# Starting from the top left
originX = -300
originY = 300

screen = turtle.Screen()
screen.tracer(0)

myMaze = turtle.Turtle()
myMaze.width(5)
myMaze.hideturtle()

myMaze.speed(0)

myMaze.penup()
myMaze.goto(originX, originY)
myMaze.pendown()
myMaze.color("#FF0000")

def Forward(distance: int, pen: Turtle):
     pen.forward(distance)

def LiftUp(distance: int, pen: Turtle):
     pen.penup()
     pen.forward(distance)
     pen.pendown()

x = originX
y = originY
for line in maze:
    for char in line:
        if char == '-':
            Forward(wallWidth, myMaze)
        else:
            LiftUp(wallWidth, myMaze)
    
    myMaze.goto(x+600, y-wallHeight)
    myMaze.penup()
    myMaze.goto(x, y)
    myMaze.pendown()

    y = y - wallHeight
    myMaze.goto(x, y)

screen.tracer(1)
input()