n, s = map(int, input().split())
a = list(map(int, input().split()))

dp = [[False] * s for _ in range(n)]
prev = [[None] * s for _ in range(n)]

if a[0] <= s:
    dp[0][a[0] - 1] = True

for i in range(1, n):
    if a[i] <= s:
        dp[i][a[i] - 1] = True
    for j in range(s):
        if dp[i - 1][j]:
            dp[i][j] = True
            prev[i][j] = j
            if j + a[i] < s:
                dp[i][j + a[i]] = True
                prev[i][j + a[i]] = j

i = 0
isYes = False
for i in range(n):
    if dp[i][-1]:
        isYes = True
        break

if isYes:
    tmp = [i, s - 1]
    route = []
    while tmp[1] is not None:
        # 選んだ時だけappend
        if prev[tmp[0]][tmp[1]] != tmp[1]:
            route.append(tmp[0] + 1)
        tmp[1] = prev[tmp[0]][tmp[1]]
        tmp[0] -= 1

    route.reverse()
    print(len(route))
    print(*route)
else:
    print(-1)
