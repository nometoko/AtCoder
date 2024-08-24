h, w = map(int, input().split())
x = []
for _ in range(h):
    x.append(list(map(int, input().split())))

sumX = [[0] * (w + 1) for _ in range(h + 1)]
for i in range(1, h + 1):
    for j in range(1, w + 1):
        sumX[i][j] = sumX[i][j - 1] + x[i - 1][j - 1]

for i in range(1, w + 1):
    for j in range(1, h + 1):
        sumX[j][i] = sumX[j - 1][i] + sumX[j][i]

q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    print(sumX[c][d] + sumX[a - 1][b - 1] - sumX[c][b - 1] - sumX[a - 1][d])
