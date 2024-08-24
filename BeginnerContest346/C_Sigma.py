n, k = map(int, input().split())
a = list(map(int, input().split()))
a = list(set(a))
ans = ((1 + k) * k) // 2
for i in a:
    if i <= k:
        ans -= i

print(ans)
