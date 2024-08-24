import bisect

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
sum_a = [0] * (n + 1)
sum_a[0] = 0
for i in range(1, n + 1):
    sum_a[i] = sum_a[i - 1] + a[i - 1]

min = 1
max = a[-1] + 1
mid = (min + max) // 2
while max - min > 1:

    mid_ind = bisect.bisect_left(a, mid)
    sum = sum_a[mid_ind] + mid * (n - mid_ind)
    # print(min, max, mid, mid_ind, sum)
    if sum > m:
        max = mid
    else:
        min = mid
    mid = (min + max) // 2

if min == a[-1]:
    print('infinite')
else:
    print(min)

# print('infinite')