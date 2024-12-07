from collections import deque
h, w, d = map(int, input().split())
grid = list(input() for _ in range(h))


def widthFirstSearch(start, dist):
    while q:
        row, col, nowDist = q.popleft()
        dist[row][col] = nowDist
        if nowDist == d:
            continue
        for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            newRow, newCol = row + dr, col + dc
            if 0 <= newRow < h and 0 <= newCol < w and grid[newRow][newCol] != '#':
                if dist[newRow][newCol] == float('inf'):
                    dist[newRow][newCol] = nowDist + 1
                    if dist[newRow][newCol] < d:
                        q.append((newRow, newCol, dist[newRow][newCol]))


distance = [[float('inf')] * w for _ in range(h)]
q = deque()
for row in range(h):
    for col in range(w):
        if grid[row][col] == 'H':
            q.append((row, col, 0))

widthFirstSearch(q, distance)

ans = 0
for row in range(h):
    print(*distance[row])
    for col in range(w):
        if distance[row][col] != float('inf'):
            ans += 1

print(ans)
