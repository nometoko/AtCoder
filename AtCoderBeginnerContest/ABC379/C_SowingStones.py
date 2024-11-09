from collections import deque

n, m = map(int, input().split())

x = list(map(int, input().split()))
a = list(map(int, input().split()))

if (sum(a) != n):
    print(-1)
    exit()

pairs = []
for i in range(m):
    pairs.append([x[i], a[i]])

pairs.sort()

ans = 0
index = 1

for i in range(m):
    if pairs[i][0] > index:
        print(-1)
        exit()
    else:
        ans += (index - pairs[i][0]) * pairs[i][1] + (pairs[i][1] - 1) * pairs[i][1] // 2
        index += pairs[i][1]

print(ans)
