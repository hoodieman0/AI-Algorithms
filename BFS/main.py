#Turtle Maze Challenge - www.101computing.net/turtle-maze/
import turtle
import maze
from BFS import DictConstructor, GetMazeFromFile, MazeStringTo2DList, MakeValidNodes, ConnectAdjacentNodes
from DrawBFS import DrawCoordinateBFS
from Graph import Graph

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

coordList = MakeValidNodes(mazeList)
graph = ConnectAdjacentNodes(DictConstructor(coordList))
myGraph = Graph(graph, False)

search = DrawCoordinateBFS(myGraph.GetGraph())
print(search.GetPath(start, end))
search.Draw(start, end, myPen)


input()





