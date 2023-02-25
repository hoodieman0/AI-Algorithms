from abc import ABC, abstractmethod

class DFS(ABC):
    def __init__(self, graph: dict) -> None:
        self.graph = graph
    
    @abstractmethod
    def SearchGraph():
        pass

class CoordinateDFS(DFS):
    def SearchGraph(self, start: tuple, goal: tuple) -> bool:
        stack = []
        visited = []

        stack.append(start)
        visited.append(start)

        i = 1
        print(str(i) + ". Frontier: " + str(stack))
        i = i + 1

        while stack:
            node = stack.pop()

            if node == goal:
                print("Hey! I reached the goal!")
                return True
            
            for key in self.graph[node].keys():
                if not key in visited:
                    stack.append(key)
                    visited.append(key)

            print(str(i) + ". Frontier: " + str(stack))
            print(str(i) + ". Visited: " + str(visited))
            i = i + 1

        return False