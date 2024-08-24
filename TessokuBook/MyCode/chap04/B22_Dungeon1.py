n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0]*n
dp[1] = a[0]
for i in range(n - 2):
    dp[i + 1] = min(dp[i + 1], dp[i] + a[i])
    dp[i + 2] = dp[i] + b[i]

dp[-1] = min(dp[-1], dp[-2] + a[-1])
print(dp[-1])
