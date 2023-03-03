#Turtle Maze Challenge - www.101computing.net/turtle-maze/
import turtle
import maze
from DrawBFS import DrawCoordinateBFS, Direction
from Graph import Graph, DictConstructor, GetMazeFromFile, MakeCoordinateNodes, ConnectAdjacentNodes
from MazeGenerator import MazeGenerator
# ==========================================================
# main.py
# Author: James Mok
# Created On: 20 Feb 2023


# Global settings

filename = "maze4.txt"
start = (2, 1)
end = (5, 9)
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

search = DrawCoordinateBFS(myGraph.GetGraph())
print(search.GetPath(start, end))
search.Draw(start, end, Direction["NORTH"], myPen)

print("~Press Any Button To Exit Program~")
input()
