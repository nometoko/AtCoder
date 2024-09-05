n, k = map(int, input().split())
a = list(map(int, input().split()))


if k % 2 == 0:
    ans = 0
    for i in range(0, k, 2):
        ans += a[i + 1] - a[i]
else:
    ans = float('inf')
    cum1 = [0] * (k // 2 + 1)
    for i in range(0, k - 1, 2):
        cum1[i // 2 + 1] = cum1[i // 2] + a[i + 1] - a[i]
    cum2 = [0] * (k // 2 + 1)
    for i in range(1, k, 2):
        cum2[i // 2 + 1] = cum2[i // 2] + a[i + 1] - a[i]
    # print(cum1, cum2)
    for i in range(k):
        if i == 0:
            weird = cum2[-1]
        elif i == k - 1:
            weird = cum1[-1] 
        elif i % 2 == 1:
            weird = cum1[i // 2] + cum2[-1] - cum2[i // 2 + 1]
            weird += a[i + 1] - a[i - 1]
        else:
            weird = cum1[i // 2] + cum2[-1] - cum2[i // 2]
        # print(weird)
        ans = min(ans, weird)

print(ans)
