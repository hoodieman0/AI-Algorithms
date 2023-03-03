# Adatped from: https://stackoverflow.com/a/51697702
# User: cdlane
# Accessed 3 March 2023
# Author: James Mok
# Created 3 March 2023

import turtle
from turtle import Turtle

# Sets the size of the maze boundaries
stamp_size = 20
scale = 3

# Functions as a C++ enum, assigns cardinal directions to numbers
Direction = {"NORTH":1, "EAST":2, "SOUTH":3, "WEST":4}



class MazeGenerator():
    def __init__(self, maze: list) -> None:
        self.maze: list = maze
     
        self.width =  len(maze[0])
        self.height = len(maze)


    # Initializes a Turtle Screen (singleton) to draw a given maze
    # using the given dimensions
    # Color is any valid hex string to color the maze boundaries
    def DrawMaze(self, color: str):
        screen = turtle.Screen()

        # Start the screen to use the specific settings of the maze
        screen.setup(self.width * stamp_size * scale, self.height * stamp_size * scale)
        screen.setworldcoordinates(-0.5, -0.5, self.width - 0.5, self.height - 0.5)

        shape = turtle.Turtle('square', visible=False)
        shape.shapesize(scale)
        shape.speed(0)
        shape.penup()
        shape.color(color)
        
        # If there is a maze boundary in the given square, draw it
        for idxY, line in enumerate(self.maze):
            for idxX, char in enumerate(line):
                if not char == '.':
                    shape.goto(idxX, idxY)
                    shape.stamp()
        
    
    # Draws the player on the Turtle Screen and returns a Turtle object of the player sprite
    # If start is not found return None
    def DrawPlayer(self, start: tuple, color: str) -> Turtle:
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()

        # Searching for the start position
        for idxY, line in enumerate(self.maze):
            for idxX, char in enumerate(line):
                if (idxX+1, idxY+1) == start and char == '.':
                    pen.goto(idxX, idxY)

                    pen.pendown()
                    pen.shape('turtle')
                    pen.color(color)
                    pen.width(5)
                    pen.left(90)
                    pen.showturtle()
                    return pen
        
        return None
