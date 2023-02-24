#Turtle Maze Challenge - www.101computing.net/turtle-maze/
import turtle
import maze
from DrawBFS import DrawCoordinateBFS, Direction
from Graph import Graph, DictConstructor, GetMazeFromFile, MakeCoordinateNodes, ConnectAdjacentNodes

# Drawing the maze
myPen=turtle.Turtle()
myPen.penup()
myPen.goto(20,-180)
myPen.pendown()
myPen.shape('turtle')
myPen.color("#DB148E")
myPen.width(5)
myPen.left(90)


#Start of maze movement

filename = "maze.txt"
start = (19,1)
end = (19,41)

mazeList = GetMazeFromFile(filename)

coordList = MakeCoordinateNodes(mazeList)
graph = ConnectAdjacentNodes(DictConstructor(coordList))
myGraph = Graph(graph, False)

search = DrawCoordinateBFS(myGraph.GetGraph())
print(search.GetPath(start, end))
search.Draw(start, end, Direction["NORTH"], myPen)

print("~Press Any Button To Exit Program~")
input()
