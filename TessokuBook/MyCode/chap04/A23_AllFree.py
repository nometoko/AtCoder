import numpy as np
n, m = map(int, input().split())

a = []
for _ in range(m):
    a.append(list(map(int, input().split())))

dp = [[np.infty] * (2 ** n) for _ in range(m)]
v = 0
for j in range(n):
    if a[0][j] == 1:
        v += 2 ** j
dp[0][v] = 1

# Initialize
for i in range(m):
    dp[i][0] = 0

# dp
for i in range(1, m):
    for j in range(2 ** n):
        if dp[i - 1][j] == np.infty:
            continue
        binJ = bin(j)[2:]
        binJ = '0' * (n - len(binJ)) + binJ
        binJ = binJ[::-1]
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        v = 0
        # binJ[k] or a[i][k]を抽出
        for k in range(n):
            if int(binJ[k]) == 1 or a[i][k] == 1:
                v += 2 ** k
        # 結局minを取るので、dp[i - 1]は見なくて良い
        # 常にj <= v
        dp[i][j] = min(dp[i][j], dp[i - 1][v])
        dp[i][v] = min(dp[i][v], dp[i - 1][j] + 1)
    # print(*dp[i])

if dp[-1][-1] == np.infty:
    print(-1)
else:
    print(dp[-1][-1])
