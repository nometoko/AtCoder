from collections import deque

n, m = map(int, input().split())

graph = dict()

for i in range(m):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = set()
    graph[a].add(b)

def widthFirstSearch(graph, start):
    visited = set()
    queue = deque()
    queue.append((start, 0))
    while len(queue) > 0:
        node, dist = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        if node in graph:
            for neighbor in graph[node]:
                if neighbor == start:
                    return dist + 1
                if neighbor not in visited:
                    queue.append((neighbor, dist + 1))
    return False


dist = widthFirstSearch(graph, 1)
if dist is not False:
    print(dist)
else:
    print(-1)
