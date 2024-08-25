n, k, d = map(int, input().split())
a = list(map(int, input().split()))

dp = [[-1] * d for _  in range(k)]

for i in range(n):
    for j in range(min(i + 1, k)  - 1, 0, -1):
        for l in range(d):
            if dp[j - 1][l] != -1:
                tmp = dp[j - 1][l] + a[i]
                dp[j][tmp % d] = max(dp[j][tmp % d], tmp)
    dp[0][a[i] % d] = max(dp[0][a[i] % d], a[i])
print(dp[-1][0])
