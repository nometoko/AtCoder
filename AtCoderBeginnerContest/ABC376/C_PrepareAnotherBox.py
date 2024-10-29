n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)
bIndex = 0
Failed = False
ans = -1

for i in range(n):
    if bIndex == n - 1:
        ans = a[-1]
    elif a[i] <= b[bIndex]:
        bIndex += 1
    else:
        if Failed is False:
            Failed = True
            ans = a[i]
        else:
            ans = -1
            break

print(ans)
