import heapq
import numpy as np


def dijkstra(start, g):
    dist = [np.infty] * n
    dist[start] = 0
    visited = [False] * n
    visited[start] = True

    queue = []
    for e in g[start]:
        heapq.heappush(queue, e)

    while queue:
        # print(queue, dist)
        cost, destination = heapq.heappop(queue)
        if visited[destination]:
            continue
        dist[destination] = cost
        visited[destination] = True
        for newDist, newDest in g[destination]:
            heapq.heappush(queue, [newDist + dist[destination], newDest])
    return dist


n = int(input())
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b, x = map(int, input().split())
    g[i].append([a, i + 1])  # [cost, destination]
    g[i].append([b, x - 1])

print(dijkstra(0, g)[-1])
