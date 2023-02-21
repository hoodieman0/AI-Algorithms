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
 