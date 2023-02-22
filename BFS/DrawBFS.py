from BFS import CoordinateBFS, MazeStringToList, MakeValidNodes, ConnectAdjacentNodes
from Graph import Graph, DictConstructor
from turtle import Turtle

# {current node : previous node}
class DrawCoordinateBFS(CoordinateBFS):

    path = {}
    def SearchForPath(self, start: tuple, goal: tuple):
        queue = []
        visited = []

        queue.append(start)
        visited.append(start)
        self.path.setdefault(start, (-1, -1))

        while queue:
            node = queue.pop(0)

            if node == goal:
                print("Hey! I reached the goal!")
                return True
            
            for key in self.graph[node].keys():
                if not key in visited:
                    queue.append(key)
                    visited.append(key)
                    self.path[key] = node
                    
        
        return False
    
    def GetPath(self, start: tuple, goal: tuple) -> list:
        self.SearchForPath(start, goal)
        sequentialPath = []
        node = self.path[goal]
        while not node is (-1, -1):
            sequentialPath.insert(0, node)
            node = self.path[node]
        return sequentialPath

    # Assume facing forward into the maze
    def Draw(self, start: tuple, goal: tuple, pen: Turtle):
        l = self.GetPath(start, goal)

        facing = "N"

        prev = l[0]
        need = "N"
        for move in l:
            a = 1
            # Move Forward

            # Move Right
                #Facing east?
                #Facing west?
            # Move Left

        print(l)

        return
    

maze = "-----.-----\n-.........-\n--.-----.--\n-.........-\n-----.-----\n-----.-----\n"
mazeList = MazeStringToList(maze)
nodeList = MakeValidNodes(mazeList)
graph = ConnectAdjacentNodes(DictConstructor(nodeList))

myGraph = Graph(graph, False)

search = CoordinateBFS(myGraph.GetGraph())

#print(search.SearchGraph((6,1), (6,6)))
myPen = Turtle()
x = DrawCoordinateBFS(myGraph.GetGraph())
x.draw((6,1), (6,6), myPen)
input()