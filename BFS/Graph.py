class Node:
    location: tuple = (int, int)
    neighbors: list = []
    
    def __init__(self, position: tuple(int, int)) -> None:
        if len(position) > 2:
            print("Coordinate not inputted: should be (x,y)")
            exit(101)
        self.location = position

    def SetNeighbor(self, node) -> None:
        if len(self.neighbors) == 4:
            print("Node " + self.location + " has an invalid insert (>4 neighbors) ")
            exit(101)
        self.neighbors.append(node)


class Graph:
    start: Node
    collection = [Node]
    height: int
    width: int

    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    def AddNeighbors(self):
        return
    
    def CreateGraph(self, graph: str):
        #9x9

        def isValidNeighbor(d: dict, x: int, y: int):
            if d[(x,y)]:
                return True
            else:
                return False

        d = {}
        j = 0
        for i in range (0, self.width*self.height):
            if graph[i] == '.':
                node = Node((i+1, j+1))
                for x in range(0, 2):
                    for k in range(0,2):
                        if isValidNeighbor(d, i+x, j+y):
                            node.SetNeighbor(d[(x,y)])
                
                d[(i+1,j+1)] = node
                j = j + 1

    
            


        
"""
-----.-----
-.........-
--.-----.--
-.........-
-----.-----

"""
        