from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))

set_a = set(a)

if len(a) % 2 == 1:
    print(a[-1])

elif len(set_a) == 1:
    if len(a) % 2 == 0:
        print(a[0], a[0] * 2)
    else:
        print(a[0])

else:
    a.sort()
    max_idx = bisect_left(a, a[-1]) - 1

    idx = 0
    if max_idx % 2 == 1:
        while idx < max_idx - idx and a[idx] + a[max_idx - idx] == a[-1]:
            idx += 1
            if idx > max_idx - idx:
                print(a[-1], end=" ")

    base_val = a[0] + a[-1]
    idx = 1
    while idx < len(a) - idx - 1 and a[idx] + a[-idx - 1] == base_val:
        idx += 1
        if idx > len(a) - idx - 1:
            print(base_val, end=" ")

    print()
