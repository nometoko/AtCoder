n = int(input())
h = list(map(int, input().split()))

dp = [0] * n
prev = [None] * n

dp[1] = abs(h[1] - h[0])
prev[1] = 0

for i in range(2, n):
    dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2]))
    if dp[i] == dp[i - 1] + abs(h[i] - h[i - 1]):
        prev[i] = i - 1
    else:
        prev[i] = i - 2

tmp = n - 1
route = []
while tmp is not None:
    route.append(tmp + 1)
    tmp = prev[tmp]

route.reverse()
print(len(route))
print(*route)
# print(dp)
# print(dp[-1])
