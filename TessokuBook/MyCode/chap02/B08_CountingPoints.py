n = int(input())
maximum = 1500
XY = [[0] * (maximum + 1) for _ in range(maximum + 1)]
for i in range(n):
    x, y = map(int, input().split())
    XY[x][y] += 1

for i in range(1, maximum + 1):
    for j in range(1, maximum + 1):
        XY[i][j] = XY[i][j-1] + XY[i][j]

for i in range(1, maximum + 1):
    for j in range(1, maximum + 1):
        XY[i][j] = XY[i - 1][j] + XY[i][j]

q = int(input())

for i in range(q):
    a, b, c, d = map(int, input().split())
    print(XY[c][d] + XY[a - 1][b - 1] - XY[a - 1][d] - XY[c][b - 1])
