h, w, n = map(int, input().split())
t = input()
gridMap = []
for _ in range(h):
    gridMap.append(input())

count = 0
for i in range(1, h - 1):
    for j in range(1, w - 1):
        if gridMap[i][j] == '#':
            continue
        xPos = j
        yPos = i
        isAns = True
        for move in t:
            if move == 'U':
                yPos -= 1
            elif move == 'D':
                yPos += 1
            elif move == 'L':
                xPos -= 1
            elif move == 'R':
                xPos += 1
            if gridMap[yPos][xPos] == '#':
                isAns = False
                break

        if isAns:
            count += 1

print(count)
