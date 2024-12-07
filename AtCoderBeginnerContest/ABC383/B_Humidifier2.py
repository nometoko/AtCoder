h, w, d = map(int, input().split())
a = list(input() for _ in range(h))

dotCount = 0
dotList = []
for row in range(len(a)):
    for c in range(len(a[row])):
        if a[row][c] == '.':
            dotCount += 1
            dotList.append([row, c])

ans = 0
for i in range(dotCount):
    humid = [False for _ in range(dotCount)]
    firstRow, firstCol = dotList[i]
    for j in range(dotCount):
        row, col = dotList[j]
        if abs(row - firstRow) + abs(col - firstCol) <= d:
            humid[j] = True

    for j in range(i + 1, dotCount):
        humidCopy = humid.copy()
        secondRow, secondCol = dotList[j]
        for k in range(dotCount):
            row, col = dotList[k]
            if abs(row - secondRow) + abs(col - secondCol) <= d:
                humidCopy[k] = True
        ans = max(ans, humidCopy.count(True))

print(ans)
