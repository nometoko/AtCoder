a, m, l, r = map(int, input().split())
dist_l = abs(l - a)
dist_r = abs(r - a)
if (l >= a >= r) or (r >= a >= l):
    print(dist_l // m + dist_r // m + 1)
else:
    if min(dist_l, dist_r) % m == 0:
        print(max(dist_l, dist_r) // m - min(dist_l, dist_r) // m + 1)
    else:
        print(max(dist_l, dist_r) // m - min(dist_l, dist_r) // m)
