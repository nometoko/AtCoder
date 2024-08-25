import bisect

n = int(input())
a = list(map(int, input().split()))
a_tmp = [[a[i], i + 1] for i in range(n)]
a_tmp.sort()
a.sort()
index = 0
for i in range(n):
    print(a_tmp[index][1], end=" ")
    index = bisect.bisect_left(a, a_tmp[index][1])

print()