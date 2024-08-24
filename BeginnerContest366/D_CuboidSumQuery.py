n = int(input())

a = [[[0] * n for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = list(map(int, input().split()))

# 3次元累積和
a_sum = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            a_sum[i][j][k] = a_sum[i][j][k - 1] + a[i - 1][j - 1][k - 1]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            a_sum[i][j][k] += a_sum[i][j - 1][k]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            a_sum[i][j][k] += a_sum[i - 1][j][k]

q = int(input())
for i in range(q):
    x1, x2, y1, y2, z1, z2 = map(int, input().split())
    print(a_sum[x2][y2][z2] - a_sum[x1 - 1][y2][z2] - a_sum[x2][y1 - 1][z2] - a_sum[x2][y2][z1 - 1] + a_sum[x1 - 1][y1 - 1][z2] + a_sum[x1 - 1][y2][z1 - 1] + a_sum[x2][y1 - 1][z1 - 1] - a_sum[x1 - 1][y1 - 1][z1 - 1])
