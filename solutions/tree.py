from rosalind import readfile, numbers
from collections import defaultdict

def explore(node, graph, explored):
    if node in explored:
        return
    explored.add(node)
    for adj in graph[node]:
        explore(adj, graph, explored)
    return

def connected_components(graph):
    explored = set()
    count = 0
    for node in graph:
        if node in explored:
            continue
        count +=1
        explore(node, graph, explored)
    return count

afile = readfile()
count = int(afile[0])
edges = map(numbers, afile[1:])
graph = defaultdict(set)
for i in range(count):
    graph[i+1] = set()
for a,b in edges:
    graph[a].add(b)
    graph[b].add(a)
print connected_components(graph)-1
