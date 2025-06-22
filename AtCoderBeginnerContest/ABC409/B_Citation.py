n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

ans = 0
for i, val in enumerate(a):
    if i < len(a) - 1 and val == a[i + 1]:
        continue

    ans = max(ans, min(i + 1, val))

print(ans)
