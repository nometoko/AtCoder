s = input()
t = input()

dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

for i in range(len(s) + 1):
    dp[i][0] = i

for j in range(len(t) + 1):
    dp[0][j] = j

for i in range(1, len(s) + 1):
    for j in range(1, len(t) + 1):
        bias = 1
        if s[i - 1] == t[j - 1]:
            bias = 0
        dp[i][j] = min(dp[i - 1][j - 1] + bias, dp[i - 1][j] + 1, dp[i][j - 1] + 1)

print(dp[-1][-1])
