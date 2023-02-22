from abc import ABC, abstractmethod #Abstract Base Class

# Helper class to streamline node creation
class Node(ABC):
    node: any = None

    @abstractmethod
    def GetNode(self):
        pass



# Helper class to streamline coordinate node creation
class CoordinateNode(Node):
    def __init__(self, xPos: int, yPos: int) -> None:
        self.node = (xPos, yPos)
    
    def GetNode(self):
        return self.node

        
"""
Graph is a dict of coordinates. The values are the distances between the nodes
Functions:
Get Graph
string to Graph
Connect Graph
Movement operations
"""


class Graph:
    isDirected = False

    # This dict must follow the format dict{node: dict{connectedNode: distanceInt}}
    # The current use case has nodes as a tuple: (xInt, yInt)
    graphDict = {}

    def __init__(self, graphDict: dict, isDirected: bool) -> None:
        self.isDirected = isDirected
        self.graphDict = graphDict
        if not self.isDirected:
            self.MakeUndirected()

    # In graphDict, sets the value of key the node1 to a tuple (node2, distance)
    def ConnectOneWay(self, node1, node2, distance) -> None:
        self.graphDict.setdefault(node1, {})[node2] = distance
    
    # For all dict keys, take their connected node and connect that node to the key
    # Eliminates the need for the input dict to have all possibilities
    def MakeUndirected(self) -> None:
        for node1 in list(self.graphDict.keys()):
            for (node2, distance) in self.graphDict[node1].items():
                self.ConnectOneWay(node2, node1, distance)

    # Returns a list of all the nodes in the graph
    def ListNodes(self) -> list:
        s1 = set([k for k in self.graphDict.keys()])
        s2 = set([k2 for v in self.graphDict.values() for k2, v2, in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

    # Returns the connected relationship graph
    def GetGraph(self) -> dict:
        return self.graphDict
        
"""
-----.-----
-.........-
--.-----.--
-.........-
-----.-----

"""
        