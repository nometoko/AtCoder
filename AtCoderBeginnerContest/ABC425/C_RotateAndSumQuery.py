n, q = map(int, input().split())

a = list(map(int, input().split()))
sum_a = [0] * len(a)
sum_a[0] = a[0]

for i, val in enumerate(a):
    if i == 0:
        continue
    sum_a[i] = sum_a[i - 1] + val

top_idx = 0
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        c = query[1]
        top_idx = (top_idx + c) % len(a)

    elif query[0] == 2:
        l, r = query[1:]
        l = (l + top_idx - 1) % len(a)
        r = (r + top_idx - 1) % len(a)
        # print(f"{l} -> {r}")
        if l <= r:
            if l == 0:
                print(sum_a[r])
            else:
                print(sum_a[r] - sum_a[l - 1])
        else:
            # l to end
            if l == 0:
                ans = sum_a[-1]
            else:
                ans = sum_a[-1] - sum_a[l - 1]
            # start to r
            ans += sum_a[r]

            print(ans)
