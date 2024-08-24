n, w = map(int, input().split())
dp = [[0] * w for _ in range(n)]

wList = [0] * n
vList = [0] * n
for i in range(n):
    wList[i], vList[i] = map(int, input().split())

if wList[0] <= w:
    dp[0][wList[0] - 1] = vList[0]

for i in range(1, n):
    for j in range(w):
        if dp[i - 1][j] != 0:
            dp[i][j] = max(dp[i - 1][j], dp[i][j])
            if j + wList[i] < w:
                dp[i][j + wList[i]] = dp[i - 1][j] + vList[i]
    if wList[i] <= w:
        dp[i][wList[i] - 1] = max(vList[i], dp[i][wList[i] - 1])

maxValue = max([max(i) for i in dp])
print(maxValue)
