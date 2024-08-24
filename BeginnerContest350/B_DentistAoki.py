n, q = map(int, input().split())
t = list(map(int, input().split()))
setT = list(set(t))
ans = len(setT)
for i in setT:
    if t.count(i) % 2 == 0:
        ans -= 1
print(n - ans)
