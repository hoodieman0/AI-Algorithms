"""
Given a maze string with . as valid nodes, and - as invalid nodes/walls, draw the maze
"""
import turtle
from turtle import Turtle
from Graph import MazeStringTo2DList, GetMazeFromFile

# Turtle board is about 600x600 pixels in size
# The origin for this is  (-300, 300), since (0, 0) is the center
# Starting from the top left
pixelDimensions = 600
originX = -300
originY = 300

# Functions as a C++ enum, assigns cardinal directions to numbers
Direction = {"NORTH":1, "EAST":2, "SOUTH":3, "WEST":4}



class MazeGenerator():
    def __init__(self, maze: list) -> None:
        self.maze: list = maze

        # How long one character is
        # Should I make the maze fixed length? (15x15 makes 40 wall length feasible)
        assert pixelDimensions % len(maze[0]) == 0
        self.wallWidth = (int)(pixelDimensions / len(maze[0]))
        self.wallHeight = self.wallWidth

    def DrawMaze(self, color: str):
        screen = turtle.Screen()
        screen.tracer(0)

        myMaze = turtle.Turtle()
        myMaze.width(5)
        myMaze.hideturtle()

        myMaze.speed(0)

        myMaze.penup()
        myMaze.goto(originX, originY)
        myMaze.pendown()
        myMaze.color(color)

        def Forward(distance: int, pen: Turtle):
            pen.forward(distance)

        def SideWall(distance: int, pen: Turtle):
            pen.right(90)
            pen.forward(distance)
            pen.left(90)

        def LiftUp(distance: int, pen: Turtle):
            pen.penup()
            pen.forward(distance)
            pen.pendown()

        x = originX
        y = originY

        for idxY, line in enumerate(self.maze):
            for idxX, char in enumerate(line):
                if idxX == 0 or idxX == len(line) - 1:
                    # No need to extend the side walls if it is the end
                    if idxY == len(maze) - 1: 
                        continue
                    SideWall(self.wallHeight, myMaze)
                    myMaze.penup()
                    myMaze.goto(x, y)
                    myMaze.pendown()
                elif char == '-':
                    Forward(self.wallWidth, myMaze)
                else:
                    LiftUp(self.wallWidth, myMaze)
                
            y = y - self.wallHeight
            myMaze.penup()
            myMaze.goto(x, y)
            myMaze.pendown()
            


        screen.tracer(1)
    
    def DrawPlayer(self, start: tuple):
        for idxY, line in enumerate(self.maze):
            for idxX, char in enumerate(line):
                if (idxX+1, idxY+1) == start:
                    
        for idxX, char in enumerate(self.maze[len(maze) - 1]):
            

        myPen=turtle.Turtle()
        myPen.penup()
        myPen.goto(20,-180)
        myPen.pendown()
        myPen.shape('turtle')
        myPen.color("#DB148E")
        myPen.width(5)
        myPen.left(90)



string = """-------.-------
-.............-
---.-------.---
-.............-
-------.-------
"""
maze = MazeStringTo2DList(string)
x = MazeGenerator(maze)
x.DrawMaze("#DB148E")
input()


input()