from BFS import CoordinateBFS
from turtle import Turtle

moveDistance = 10

# {current node : previous node}
class DrawCoordinateBFS(CoordinateBFS):

    path = {}
    def SearchForPath(self, start: tuple, goal: tuple):
        self.path = {}
        queue = []
        visited = []

        queue.append(start)
        visited.append(start)
        self.path.setdefault(start, (-1, -1))

        while queue:
            node = queue.pop(0)

            if node == goal:
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
        sequentialPath.append(goal)
        node = self.path[goal]
        while node != (-1, -1):
            sequentialPath.append(node)
            node = self.path[node]
        sequentialPath.reverse()
        return sequentialPath


    # Assume facing forward into the maze
    def Draw(self, start: tuple, goal: tuple, pen: Turtle):
        
        Direction = {"NORTH":1, "EAST":2, "SOUTH":3, "WEST":4}

        def Forward(pen: Turtle):
            pen.forward(moveDistance)
        
        def Right(pen: Turtle):
            pen.right(90)
        
        def Left(pen: Turtle):
            pen.left(90)
        
        def Movement(node: tuple, next: tuple, facing: int):
            x = next[0] - node[0] 
            y = next[1]- node[1] 
            print(str(node) + " -> " + str(next))

            if y > 0:
                change = Direction["NORTH"]
                print("MOVING NORTH")
            elif y < 0:
                change = Direction["SOUTH"]
                print("MOVING SOUTH")
            elif x > 0:
                change = Direction["EAST"]
                print("MOVING EAST")
            elif x < 0:
                change = Direction["WEST"]
                print("MOVING WEST")
            else:
                print("INVALID NODES -> Movement() : DrawBFS.py")
                return

            z = change - facing
            while not z == 0:
                if z > 2:
                    z = 0
                    Left(pen)
                elif z < -2:
                    z = 0
                    Right(pen)
                elif z > 0:
                    Right(pen)
                    z = z - 1
                elif z < 0:
                    Left(pen)
                    z = z + 1
            
            Forward(pen)
            print("\n-------------------------")
            return change

        pathList = self.GetPath(start, goal)
        
        facing = Direction["NORTH"]

        prev = pathList[0]
        for move in pathList[1:]:
            facing = Movement(prev, move, facing)
            prev = move
        
        print("Finished Drawing Path!")
    

