h, w = map(int, input().split())
Map = []
for _ in range(h):
    Map.append(input())

dp = [[0] * w for _ in range(h)]

# Initialize
isSharp = False
for i in range(h):
    if Map[i][0] == '#':
        isSharp = True
    if isSharp is False:
        dp[i][0] = 1
    else:
        dp[i][0] = 0

isSharp = False
for i in range(w):
    if Map[0][i] == '#':
        isSharp = True
    if isSharp is False:
        dp[0][i] = 1
    else:
        dp[0][i] = 0

for i in range(1, h):
    for j in range(1, w):
        if Map[i][j] == '.':
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        else:
            dp[i][j] = 0

print(dp[-1][-1])
