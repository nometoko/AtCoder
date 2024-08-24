import numpy as np
n, w = map(int, input().split())
wList = [0] * n
vList = [0] * n


for i in range(n):
    wList[i], vList[i] = map(int, input().split())

vSum = sum(vList)
dp = [[np.infty] * vSum for _ in range(n)]
nonZeroList = []
if wList[0] <= w:
    dp[0][vList[0] - 1] = wList[0]

for i in range(1, n):
    if wList[i] <= w:
        dp[i][vList[i] - 1] = wList[i]
    for j in range(vSum):
        if dp[i - 1][j] != np.infty:
            dp[i][j] = min(dp[i - 1][j], dp[i][j])
            # print(dp[i][j] + wList[i])
            if dp[i - 1][j] + wList[i] <= w:
                # dp[i]行を参照してはいけない
                dp[i][j + vList[i]] = min(dp[i - 1][j + vList[i]], dp[i - 1][j] + wList[i])

# i = 0
# for i in reversed(range(vSum)):
#     if dp[-1][i] != np.infty:
#         break

# route = []
# hist = []
# for j in reversed(range(n)):
#     if i == -1:
#         break
#     if dp[j][i] != dp[j - 1][i]:
#         print(dp[j][i])
        # route.append(j + 1)
        # hist.append(dp[j][i])
        # i -= vList[j]
# route.reverse()
# hist.reverse()
# print(route)
# print(hist)

for i in dp:
    print(*i)

for i in reversed(range(vSum)):
    if dp[-1][i] != np.infty:
        print(i + 1)
        exit(0)
