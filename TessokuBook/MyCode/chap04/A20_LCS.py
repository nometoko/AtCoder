s = input()
t = input()

dp = [[0] * len(t) for _ in range(len(s))]

if s[0] == t[0]:
    dp[0][0] = 1

for i in range(1, len(s)):
    if s[i] == t[0]:
        dp[i][0] = 1
    else:
        dp[i][0] = dp[i-1][0]

for j in range(1, len(t)):
    if s[0] == t[j]:
        dp[0][j] = 1
    else:
        dp[0][j] = dp[0][j-1]

for i in range(1, len(s)):
    for j in range(1, len(t)):
        if i == j == 0:
            continue
        if s[i] == t[j]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# for i in dp:
#     print(*i)
print(dp[-1][-1])
