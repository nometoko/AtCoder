import numpy as np
t = input()
n = int(input())

lenT = len(t)
dp = [[np.infty] * (lenT + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    s = list(input().split())
    for j in range(1, lenT + 1):
        if dp[i - 1][j] != np.infty:
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
            for strings in s[1:]:
                lenS = len(strings)
                if t[j: j + lenS] == strings:
                    dp[i][j + lenS] = min(dp[i][j + lenS], dp[i - 1][j] + 1)
    for strings in s[1:]:
        lenS = len(strings)
        if t[:lenS] == strings:
            dp[i][lenS] = 1


# for tmp in dp:
#     print(*tmp)
if dp[-1][-1] == np.infty:
    print(-1)
else:
    print(dp[-1][-1])
