#Turtle Maze Challenge - www.101computing.net/turtle-maze/
import turtle
import maze
from DrawDFS import DrawCoordinateDFS, Direction
from Graph import Graph, DictConstructor, GetMazeFromFile, MakeCoordinateNodes, ConnectAdjacentNodes
from MazeGenerator import MazeGenerator

# Drawing the maze
myPen=turtle.Turtle()
myPen.penup()
myPen.goto(20,-180)
myPen.pendown()
myPen.shape('turtle')
myPen.color("#DB148E")
myPen.width(5)
myPen.left(90)

# ==========================================================
# main.py
# Author: James Mok
# Created On: 20 Feb 2023

# Global settings

filename = "maze2.txt"
start = (8, 1)
end = (8, 15)
mazeColor = "#00c8ff"
playerColor = "red"

# Transform file into a list
mazeList = GetMazeFromFile(filename)


# Generate maze drawing with player

drawing = MazeGenerator(mazeList)
drawing.DrawMaze(mazeColor)
myPen = drawing.DrawPlayer(start, playerColor)


# Create Graph

coordList = MakeCoordinateNodes(mazeList)
graph = ConnectAdjacentNodes(DictConstructor(coordList))
myGraph = Graph(graph, False)


# Start of maze movement

search = DrawCoordinateDFS(myGraph.GetGraph())
print(search.GetPath(start, end))
search.Draw(start, end, Direction["NORTH"], myPen)

print("~Press Any Button To Exit Program~")
input()

