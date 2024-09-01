n = int(input())
a = list(map(int, input().split()))
a = [0] + a + [0]
min1 = [0] * (n + 1)
min2 = [0] * (n + 1)
min1[0] = min(a[0], a[1] - 1)
min2[-1] = min(a[-1] + n + 1, a[-2] + n)
for i in range(1, n + 1):
    min1[i] = min(min1[i - 1], a[i + 1] - (i + 1))
    min2[-i - 1] = min(min2[-i], a[-i - 2] + n + 1 - (i + 1))

ans = -1
for k in range(0, n):
    ans = max(ans, min(min1[k] + k + 1, min2[k + 1] - (k + 1)))

print(ans)
