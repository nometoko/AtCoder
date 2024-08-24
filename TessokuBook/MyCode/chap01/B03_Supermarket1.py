n = int(input())
a = list(map(int, input().split()))
check = 1000

isBreak = False
ans = False
for i in range(n):
    for j in range(i + 1, n):
        tmp = check - a[i] - a[j]
        if check - a[i] - a[j] in a:
            if tmp == a[i] and a.count(a[i]) == 1:
                continue
            if tmp == a[j] and a.count(a[j]) == 1:
                continue
            ans = True
            isBreak = True
            break
    if isBreak:
        break

if ans:
    print("Yes")
else:
    print("No")
