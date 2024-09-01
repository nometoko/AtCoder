n = int(input())
a = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(n)]

dp[0][0] = 0
dp[0][1] = a[0]

if n > 1:
    dp[1][0] = a[0] + a[1] * 2
    dp[1][1] = a[1]

if n > 2:
    for i in range(2, n):
        dp[i][0] = max(dp[i - 1][1] + a[i] * 2, dp[i - 2][1] + a[i] * 2)
        dp[i][1] = max(dp[i - 1][0] + a[i], dp[i - 2][0] + a[i])
        # print(dp)

print(max(dp[n - 1]))

