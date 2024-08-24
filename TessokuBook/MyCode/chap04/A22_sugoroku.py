n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0] * n
for i in range(n - 1):
    # そのマスを訪れていなかった場合、計算しない
    if dp[i] == 0 and i != 0:
        continue
    dp[a[i] - 1] = max(dp[a[i] - 1], dp[i] + 100)
    dp[b[i] - 1] = max(dp[b[i] - 1], dp[i] + 150)

print(dp[-1])
