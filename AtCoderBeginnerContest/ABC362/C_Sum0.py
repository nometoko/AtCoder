n = int(input())
xMin = 0
xMax = 0
lr = []
for _ in range(n):
    l, r = map(int, input().split())
    lr.append([l, r])
    xMin += l
    xMax += r

if xMin <= 0 <= xMax:
    print('Yes')
    diff = xMax
    for i in range(n):
        l, r = lr[i][0], lr[i][1]
        ans = max(l, r - diff)
        print(ans, end=' ')
        diff -= r - ans
else:
    print('No')
