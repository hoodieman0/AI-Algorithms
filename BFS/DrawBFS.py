# DrawBFS.py
# Author: James Mok
# Created On: 22 Feb 2023

from BFS import CoordinateBFS
from turtle import Turtle


# Functions as a C++ enum, assigns cardinal directions to numbers
Direction = {"NORTH":1, "EAST":2, "SOUTH":3, "WEST":4}

# Takes the CoordinateBFS class and modifies it to draw the found path
class DrawCoordinateBFS(CoordinateBFS):

    # path is of the format: dict{tuple(current node) : tuple(previous node)}
    path = {}

    # How far to draw on the Turtle graphic
    moveDistance = 1

    def SetMoveDistance(self, distance: int):
        self.moveDistance = distance

    # Regular BFS search from CoordinateBFS, with the exception
    # that the path dictionary is updated for each node
    # Returns true if BFS found a path
    # Returns false if there is not path from start to goal
    # The start of the path is denoted by (-1, -1)
    def SearchForPath(self, start: tuple, goal: tuple) -> bool:
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
    

    # Given a starting and end point, get the path BFS took to get to the end
    # Returns a list where the first element is the start, and successive elements
    # are next move BFS took
    # The start of the path is denoted by (-1, -1)
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
    # Calls GetPath() and draws the path found using Python Turtle
    def Draw(self, start: tuple, goal: tuple, facing: int, pen: Turtle):
        # Move the player forward in the pen variable
        def Forward(pen: Turtle):
            pen.forward(self.moveDistance)
        

        # Rotate the player 90 degrees to the right in the pen variable
        def Right(pen: Turtle):
            pen.right(90)
        

        # Rotate the player 90 degrees to the left in the pen variable
        def Left(pen: Turtle):
            pen.left(90)
        

        # Determines which way the player should face and moves forward
        # Takes the initial cardinal direction, and calculates if the cardinal direction needs to change
        # Returns the new cardinal direction that the player is facing
        # Node is the current place in the path, next is the next node in the path
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
                print("INVALID NODES -> Movement("+ str(node) + ", " + str(node) + ", " + str(facing) + ") : DrawBFS.py")
                return

            turns = change - facing
            while not turns == 0:
                # If the distance is requires 3 or more turns in one direction, do 1 turn in the opposite direction
                if turns > 2: 
                    turns = 0
                    Left(pen)
                elif turns < -2:
                    turns = 0
                    Right(pen)
                # Else do the correct turn
                elif turns > 0:
                    Right(pen)
                    turns = turns - 1
                elif turns < 0:
                    Left(pen)
                    turns = turns + 1
            
            # After correcting the cardinal direction, go forward
            Forward(pen)
            print("\n-------------------------")
            return change # Report the new facing direction

        pathList = self.GetPath(start, goal)
        
        prev = pathList[0]
        for move in pathList[1:]:
            facing = Movement(prev, move, facing)
            prev = move
        
        print("Finished Drawing Path!")
