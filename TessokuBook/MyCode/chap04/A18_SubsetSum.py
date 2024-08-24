n, s = map(int, input().split())
a = list(map(int, input().split()))

# n * s の行列
# i番目のカードまでで取ることの出来る値にはtrueが入る
dp = [[False] * s for _ in range(n)]

if a[0] <= s:
    dp[0][a[0] - 1] = True
for i in range(1, n):
    for j in range(s):
        if dp[i - 1][j]:
            dp[i][j] = True
            if j + a[i] < s:
                dp[i][j + a[i]] = True
    if a[i] <= s:
        dp[i][a[i] - 1] = True

isYes = False
for i in range(1, n):
    if dp[i][-1]:
        isYes = True
        break

if isYes:
    print("Yes")
else:
    print("No")
