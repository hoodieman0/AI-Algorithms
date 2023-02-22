from Graph import Graph, CoordinateNode, DictConstructor
from abc import ABC, abstractmethod

# Breadth First Search Base Class
class BFS(ABC):
    def __init__(self, graph, start, goal) -> None:
        self.graph = graph
        self.start = start
        self.goal = goal
    
    @abstractmethod
    def SearchGraph():
        pass

# BFS using (x, y) coordinate system
class CoordinateBFS(BFS):
    def SearchGraph(self):
        queue = []
        visited = []

        queue.append(self.start)
        visited.append(self.start)
        i = 1
        print(str(i) + ". Frontier: " + str(queue))
        i = i + 1

        while queue:
            node = queue.pop(0)
            print("\n@("+ str(node[0])+", " + str(node[1]) + ")")
            #visited.append(node)

            if node == self.goal:
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




maze = "-----.-----\n-.........-\n--.-----.--\n-.........-\n-----.-----\n-----.-----\n"
file = open("output.txt", "w")



mazeList = []
temp = []
for c in maze:
    if c == '\n':
        mazeList.append(temp)
        temp = []
        continue
    temp.append(c)

#print(mazeList)
#file.write(str(mazeList))

newNodes = []
for idxY, lst in enumerate(mazeList):
    for idxX, char in enumerate(lst):
        if char == ".":
            newNodes.append((idxX+1, idxY+1))
            # WHY NOT JUST MAKE THIS A DICT

#print(newNodes)

graph = DictConstructor(newNodes)
for key in graph.keys():
    if (key[0] - 1, key[1]) in graph:
        graph[key][key[0] - 1, key[1]] = 1
    if (key[0] + 1, key[1]) in graph:
        graph[key][key[0] + 1, key[1]] = 1
    if (key[0], key[1] - 1) in graph:
        graph[key][key[0], key[1] - 1] = 1
    if (key[0], key[1] + 1) in graph:
        graph[key][key[0], key[1] + 1] = 1

#print(graph)


myGraph = Graph(graph, False)
print(CoordinateBFS(myGraph.GetGraph(), (6,1), (6,6)))
file.close()





