# Adatped from: https://stackoverflow.com/a/51697702
# User: cdlane
# Accessed 3 March 2023


import turtle
from turtle import Turtle
from Graph import MazeStringTo2DList, GetMazeFromFile

stamp_size = 20
scale = 3

# Functions as a C++ enum, assigns cardinal directions to numbers
Direction = {"NORTH":1, "EAST":2, "SOUTH":3, "WEST":4}



class MazeGenerator():
    def __init__(self, maze: list) -> None:
        self.maze: list = maze

        # Should I make the maze fixed length? (15x15 makes 40 wall length feasible)        
        self.width =  len(maze[0])
        self.height = len(maze)

        """assert not len(self.maze[0]) % 2 == 0 # Makes sure the maze is odd (has a middle point to center on (0, 0))
        assert self.wallWidth * len(maze[0]) <= pixelDimensions
        assert self.wallHeight * len(maze) <= pixelDimensions"""

    def DrawMaze(self, color: str):
        screen = turtle.Screen()
        screen.setup(self.width * stamp_size * scale, self.height * stamp_size * scale)
        screen.setworldcoordinates(-0.5, -0.5, self.width - 0.5, self.height - 0.5)
        screen.tracer(0)

        shape = turtle.Turtle('square', visible=False)
        shape.shapesize(scale)
        shape.speed(0)
        shape.penup()
        shape.color(color)
        
        for idxY, line in enumerate(self.maze):
            for idxX, char in enumerate(line):
                if not char == '.':
                    shape.goto(idxX, idxY)
                    shape.stamp()
        
        screen.tracer(1)
    
    def DrawPlayer(self, start: tuple, color: str) -> Turtle:
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()

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
