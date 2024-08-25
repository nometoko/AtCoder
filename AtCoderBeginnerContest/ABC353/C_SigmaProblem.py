import bisect

n = int(input())
a = list(map(int, input().split()))
a.sort()
div = int(1e8)
ans = sum(a) * (n - 1)
half = bisect.bisect_left(a, div // 2)
ans -= (n - half) * (n - half - 1) // 2 * div

for i in range(half):
    limit = div - a[i]
    limitIndex = bisect.bisect_left(a, limit)
    ans -= div * (n - limitIndex)

print(ans)
