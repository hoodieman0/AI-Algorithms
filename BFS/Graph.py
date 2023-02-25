# Graph.py
# Author: James Mok
# Created On: 20 Feb 2023

from abc import ABC # Abstract Base Class

# Helper class to streamline node creation
class Node(ABC):
    node: any = None

    def GetNode(self):
        return self.node


# Helper class to streamline COORDINATE node creation
class CoordinateNode(Node):
    def __init__(self, xPos: int, yPos: int) -> None:
        self.node = (xPos, yPos)

        
# Constructs the proper dictionary given a list of nodes
# Note: the nodes must be connected using ConnectOneWay()
def DictConstructor(nodeList: list) -> dict:
    graphDict = {}
    for node in nodeList:
        graphDict[node] = {}
    return graphDict


# Takes a string that represents a maze and returns a 2D list of chars
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


# Opens a file and returns a 2D list of chars that represents the maze
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


# Takes a 2D list of a maze and assigns valid nodes to tuples of the format (x, y)
# Should be paired with the function MazeStringTo2DList() or GetMazeFromFile()
# All period('.') characters are considered valid nodes
def MakeCoordinateNodes(mazeList: list) -> list:
    newNodes = []
    for idxY, lst in enumerate(mazeList):
        for idxX, char in enumerate(lst):
            if char == ".":
                newNodes.append((idxX+1, idxY+1))
    
    return newNodes


# Takes in a dictionary and looks for nodes in the adjacent x and y coordinates
# This function reformats the graph to form connections that may or may not exist
# Should only be paired with the function MakeCoordinateNodes() or similar coordinate plane graphs
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


class Graph:
    isDirected = False

    # This dict must follow the format dict{node: dict{connectedNode: distanceInt}}
    graphDict = {}


    # The input graphDict can be a properly formatted dict
    def __init__(self, graphDict: dict, isDirected: bool) -> None:
        self.isDirected = isDirected
        self.graphDict = graphDict
        # Not necessary due to helper functions, but could be useful
        #if not self.isDirected:
            #self.MakeUndirected()


    # In graphDict, sets the value of key the node1 to a tuple (node2, distance)
    # node1 and node2 must be in the graphDict
    def ConnectOneWay(self, node1: tuple, node2: tuple, distance: int) -> None:
        self.graphDict.setdefault(node1, {})[node2] = distance
    

    # For all dict keys, take their connected node and connect that node to the key
    # Eliminates the need for the input dict to have all connection possibilities
    def MakeUndirected(self) -> None:
        for node1 in list(self.graphDict.keys()):
            for (node2, distance) in self.graphDict[node1].items():
                self.ConnectOneWay(node2, node1, distance)


    # Returns a list of all the nodes in the graph
    # Each node is visited only once
    def ListNodes(self) -> list:
        s1 = set([k for k in self.graphDict.keys()])
        s2 = set([k2 for v in self.graphDict.values() for k2, v2, in v.items()])
        nodes = s1.union(s2)
        return list(nodes)


    # Returns the connection relationship graph
    def GetGraph(self) -> dict:
        return self.graphDict
        