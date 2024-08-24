n = int(input())
pa = []
for i in range(n):
    pa.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]

for length in reversed(range(1, n)):
    for left in range(n - length + 1):
        right = left + length - 1
        leftScore = 0
        rightScore = 0
        if left != 0 and left + 1 <= pa[left - 1][0] <= right + 1:
            leftScore = pa[left - 1][1]
        if right != n - 1 and left + 1 <= pa[right + 1][0] <= right + 1:
            rightScore = pa[right + 1][1]
        # print(left, right, leftScore, rightScore)
        if left == 0:
            dp[left][right] = dp[left][right + 1] + rightScore
        elif right == n - 1:
            dp[left][right] = dp[left - 1][right] + leftScore
        else:
            dp[left][right] = max(dp[left - 1][right] + leftScore, dp[left][right + 1] + rightScore)


# for i in dp:
#     print(*i)

ans = 0
for i in range(n):
    ans = max(ans, dp[i][i])
print(ans)
