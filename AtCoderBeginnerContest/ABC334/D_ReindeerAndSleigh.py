import bisect

n, q = map(int, input().split())
r = list(map(int, input().split()))
r.sort()

r_cum = [0] * n
r_cum[0] = r[0]
for i in range(1, n):
    r_cum[i] = r_cum[i - 1] + r[i]

for i in range(q):
    x = int(input())
    print(bisect.bisect_right(r_cum, x))
