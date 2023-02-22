from Graph import Graph, CoordinateNode

g = {(1,1):{(1,2): 1}, (9,9):{(1,2): 1}}

maze = """
-----.-----\n
-.........-\n
--.-----.--\n
-.........-\n
-----.-----\n
-----.-----\n
"""

w = []
temp = []
for c in maze:
    if c == '\n':
        w.append(temp)
        temp = []
        continue
    temp.append(c)

print(w)

newNodes = []
for idxX, lst in enumerate(w):
    for idxY, char in enumerate(lst):
        if char == ".":
            newNodes.append((idxX+1, idxY+1))

print(newNodes)


myGraph = Graph({}, False)
myGraph.DictConstructor(newNodes)
