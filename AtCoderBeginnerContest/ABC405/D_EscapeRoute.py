from collections import deque
import re


def movable(pos, grid, h, w):
    y, x = pos

    if 0 <= y < h and 0 <= x < w and grid[y][x] == ".":
        return True

    return False


def dfs(q, grid, h, w):
    moves = [[0, 1, "<"], [1, 0, "^"], [-1, 0, "v"], [0, -1, ">"]]

    while q:
        pos = q.popleft()
        y, x = pos

        for dy, dx, dire in moves:
            new_y = y + dy
            new_x = x + dx
            new_pos = (new_y, new_x)
            if movable(new_pos, grid, h, w):
                grid[new_y][new_x] = dire
                q.append((new_y, new_x))

    return


h, w = map(int, input().split())

grid = [list(input()) for _ in range(h)]


q = deque()
for i, row in enumerate(grid):
    for j, char in enumerate(row):
        if char == "E":
            q.append((i, j))

if len(q) == 0:
    for row in grid:
        print("".join(row))
    exit()

dfs(q, grid, h, w)

for row in grid:
    print("".join(row))
