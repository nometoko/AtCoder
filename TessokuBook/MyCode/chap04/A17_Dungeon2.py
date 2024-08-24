n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0] * n
prev = [0] * n

dp[1] = a[0]
prev[1] = 0

for i in range(2, n):
    dp[i] = min(dp[i - 1] + a[i - 1], dp[i - 2] + b[i - 2])
    if dp[i] == dp[i - 1] + a[i - 1]:
        prev[i] = i - 1
    else:
        prev[i] = i - 2

tmp = n - 1
route = []
while tmp != 0:
    route.append(tmp + 1)
    tmp = prev[tmp]

route.append(1)
route.reverse()
print(len(route))
print(*route)
