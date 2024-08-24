import bisect

n = int(input())
a = list(map(int, input().split()))

l = []
l.append(a[0])

for i in range(1, n):
    index = bisect.bisect_left(l, a[i])
    if index == len(l):
        l.append(a[i])
    else:
        l[index] = a[i]

print(len(l))
