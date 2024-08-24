maxRange = 1501

paperMap = [[0] * maxRange for _ in range(maxRange)]
n = int(input())
for i in range(n):
    a, b, c, d = map(int, input().split())
    paperMap[a][b] += 1
    paperMap[a][d] -= 1
    paperMap[c][b] -= 1
    paperMap[c][d] += 1

for i in range(maxRange):
    for j in range(1, maxRange):
        paperMap[i][j] += paperMap[i][j - 1]

for i in range(1, maxRange):
    for j in range(maxRange):
        paperMap[i][j] += paperMap[i - 1][j]

area = 0
for i in range(maxRange):
    for j in range(maxRange):
        if paperMap[i][j] >= 1:
            area += 1

print(area)
