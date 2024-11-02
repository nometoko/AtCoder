a = list(map(int, input().split()))
seta = set(a)

ans = 0
for tmpa in seta:
    if a.count(tmpa) == 2 or a.count(tmpa) == 3:
        ans += 1
    elif a.count(tmpa) == 4:
        ans += 2

print(ans)
