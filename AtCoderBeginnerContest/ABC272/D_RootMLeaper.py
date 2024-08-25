from math import sqrt
from collections import deque


n, m = map(int, input().split())
dist = int(sqrt(m))
a = [[-1] * n for _ in range(n)]
sign_x = [1, 1, -1, -1]
sign_y = [1, -1, 1, -1]
move = set()

for dx in range(dist + 1):
    tmp = m - (dx ** 2)
    if int(sqrt(tmp)) ** 2 == tmp:
        dy = int(sqrt(tmp))
        for i in range(4):
            move.add((sign_x[i] * dx, sign_y[i] * dy))

len_move = len(move)
search = deque()
search.append((0, 0, 0))

while search:
    x, y, depth = search.popleft()
    if a[x][y] != -1:
        continue
    a[x][y] = depth
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] == -1:
                search.append((nx, ny, depth + 1))

for tmp in a:
    print(*tmp)
