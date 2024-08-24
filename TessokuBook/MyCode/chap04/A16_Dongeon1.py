n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0] * n
dp[1] = a[0]
for i in range(1, n - 1):
    dp[i + 1] = min(dp[i] + a[i], dp[i - 1] + b[i - 1])

print(dp[n - 1])
