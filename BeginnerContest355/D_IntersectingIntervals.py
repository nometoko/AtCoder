import bisect

n = int(input())
l = [0] * n
r = [0] * n
for i in range(n):
    l[i], r[i] = map(int, input().split())

l.sort()
r.sort()

ans = n * (n - 1) // 2
for i in range(n):
    l_index = bisect.bisect_left(r, l[i])
    ans -= l_index

print(ans)
