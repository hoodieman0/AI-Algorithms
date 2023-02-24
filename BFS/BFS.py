from abc import ABC, abstractmethod

# Breadth First Search Base Class
# Helper class to define needed functions for BFS classes
class BFS(ABC):
    def __init__(self, graph: dict) -> None:
        self.graph = graph
    
    @abstractmethod
    def SearchGraph():
        pass

# BFS using (x, y) coordinate system
# The data type should be a tuple with two ints (x, y)
class CoordinateBFS(BFS):

    # This is the BFS algorithm with guiding print statements
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
