from Graph import Graph, CoordinateNode, DictConstructor

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

print(graph)


myGraph = Graph(graph, False)
file.close()


# Breadth First Search
#
class BFS:


