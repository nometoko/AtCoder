h, w, n = map(int, input().split())
gridMap = [['.'] * w for _ in range(h)]
pos = [0, 0]
direction = ['up', 'left', 'down', 'right']
directionIndex = 0
for _ in range(n):
    # white → black
    if gridMap[pos[0]][pos[1]] == '.':
        gridMap[pos[0]][pos[1]] = '#'
        directionIndex = (directionIndex - 1) % 4
    else:
        gridMap[pos[0]][pos[1]] = '.'
        directionIndex = (directionIndex + 1) % 4

    if direction[directionIndex] == 'up':
        pos[0] = (pos[0] - 1) % h
    elif direction[directionIndex] == 'down':
        pos[0] = (pos[0] + 1) % h
    elif direction[directionIndex] == 'left':
        pos[1] = (pos[1] - 1) % w
    else:
        pos[1] = (pos[1] + 1) % w

for tmp in gridMap:
    print(*tmp, sep='')
