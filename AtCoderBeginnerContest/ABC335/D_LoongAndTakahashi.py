n = int(input())

mode = 0
pos = [0, 0]
grid = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n ** 2):
    # print(grid)
    grid[pos[0]][pos[1]] = i + 1
    if mode == 0:
        pos[0] += 1
        if pos[0] >= n or grid[pos[0]][pos[1]] != 0:
            mode = 1
            pos[0] -= 1
            pos[1] += 1
    elif mode == 1:
        pos[1] += 1
        if pos[1] >= n or grid[pos[0]][pos[1]] != 0:
            mode = 2
            pos[1] -= 1
            pos[0] -= 1
    elif mode == 2:
        pos[0] -= 1
        if pos[0] < 0 or grid[pos[0]][pos[1]] != 0:
            mode = 3
            pos[0] += 1
            pos[1] -= 1
    else:
        pos[1] -= 1
        if pos[1] < 0 or grid[pos[0]][pos[1]] != 0:
            mode = 0
            pos[1] += 1
            pos[0] += 1

grid[(n - 1) // 2][(n - 1) // 2] = 'T'
for tmp in grid:
    print(*tmp)
