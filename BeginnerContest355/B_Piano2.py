n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()

if n - m > 1:
    print('Yes')
else:
    aIndex = 0
    bIndex = 0
    if a[0] > b[0]:
        bIndex += 1
        pre = 1
    else:
        aIndex += 1
        pre = 0

    while aIndex < n and bIndex < m:
        if aIndex == n - 1:
            bIndex += 1
            pre = 1
            continue
        if bIndex == m - 1:
            if pre == 0:
                print('Yes')
                exit(0)
            aIndex += 1
            pre = 0
            continue

        if a[aIndex] > b[bIndex]:
            bIndex += 1
            pre = 1
        else:
            if pre == 0:
                print('Yes')
                exit(0)
            aIndex += 1
            pre = 0
    print('No')
