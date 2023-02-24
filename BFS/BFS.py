from Graph import Graph, CoordinateNode, DictConstructor
from abc import ABC, abstractmethod

# Breadth First Search Base Class
class BFS(ABC):
    def __init__(self, graph: dict) -> None:
        self.graph = graph
    
    @abstractmethod
    def SearchGraph():
        pass

# BFS using (x, y) coordinate system
class CoordinateBFS(BFS):
    def SearchGraph(self, start: tuple, goal: tuple):
        queue = []
        visited = []

        queue.append(start)
        visited.append(start)
        i = 1
        print(str(i) + ". Frontier: " + str(queue))
        i = i + 1

        while queue:
            node = queue.pop(0)
            print("\n@("+ str(node[0])+", " + str(node[1]) + ")")

            if node == goal:
                print("Hey! I reached the goal!")
                return True
            
            for key in self.graph[node].keys():
                if not key in visited:
                    queue.append(key)
                    visited.append(key)
                

            print(str(i) + ". Frontier: " + str(queue))
            print(str(i) + ". Visited: " + str(visited))
            i = i + 1
        
        return False



def MazeStringTo2DList(maze: str) -> list:
    mazeList = []
    temp = []
    for c in maze:
        if c == '\n':
            mazeList.append(temp)
            temp = []
            continue
        temp.append(c)

    mazeList.reverse()
    return mazeList

def GetMazeFromFile(filename: str) -> list:
    with open(filename) as file:
        content = file.readlines()
    mazeList = []
    temp = []
    for string in content:
        for c in string:
            if c == '\n':
                mazeList.append(temp)
                temp = []
                continue
            temp.append(c)

    mazeList.reverse()
    return mazeList


def MakeValidNodes(mazeList: list) -> list:
    newNodes = []
    for idxY, lst in enumerate(mazeList):
        for idxX, char in enumerate(lst):
            if char == ".":
                newNodes.append((idxX+1, idxY+1))
    
    return newNodes

def ConnectAdjacentNodes(graph: dict) -> dict:    
    for key in graph.keys():
        if (key[0] - 1, key[1]) in graph:
            graph[key][key[0] - 1, key[1]] = 1
        if (key[0] + 1, key[1]) in graph:
            graph[key][key[0] + 1, key[1]] = 1
        if (key[0], key[1] - 1) in graph:
            graph[key][key[0], key[1] - 1] = 1
        if (key[0], key[1] + 1) in graph:
            graph[key][key[0], key[1] + 1] = 1

    return graph
