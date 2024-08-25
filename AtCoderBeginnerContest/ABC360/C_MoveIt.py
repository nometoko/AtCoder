n = int(input())
a = list(map(int, input().split()))
w = list(map(int, input().split()))

aw = [[a[i], w[i]] for i in range(n)]
aw.sort()

ans = 0
for i in range(n - 1):
    if aw[i][0] == aw[i + 1][0]:
        ans += aw[i][1]

print(ans)
