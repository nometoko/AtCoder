import bisect

n, q = map(int, input().split())
a = list(map(int, input().split()))

def check(a, b, x, k):
    left_ind = bisect.bisect_left(a, b - x)
    right_ind = bisect.bisect_right(a, b + x)
    return right_ind - left_ind >= k

a.sort()

for i in range(q):
    b, k = map(int, input().split())
    x_min = 0
    x_max = max(b - a[0], a[-1] - b)

    while x_max - x_min > 1:
        x_mid = (x_min + x_max) // 2
        if check(a, b, x_mid, k):
            x_max = x_mid
        else:
            x_min = x_mid
    print(x_max)
