from abc import ABC, abstractmethod

class DFS(ABC):
    def __init__(self, graph: dict) -> None:
        self.graph = graph
    
    @abstractmethod
    def SearchGraph():
        pass