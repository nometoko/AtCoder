n, t, p = map(int, input().split())
l = list(map(int, input().split()))

l.sort()
l.reverse()
print(max(0, t - l[p - 1]))
