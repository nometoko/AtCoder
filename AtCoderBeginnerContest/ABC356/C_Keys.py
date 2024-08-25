n, m, k = map(int, input().split())

c = [0] * m
keys = []
result = [False] * m
for i in range(m):
    tmp = list(input().split())
    c[i] = int(tmp[0])
    keys.append([int(tmp[i]) for i in range(1, c[i] + 1)])
    if tmp[-1] == 'o':
        result[i] = True

ans = 0
for i in range(2 ** n):
    isAns = True
    for j in range(m):
        keyCount = 0
        binI = bin(i)[2:]
        binI = '0' * (n - len(binI)) + binI
        binI = binI[::-1]
        for key in keys[j]:
            if binI[key - 1] == '1':
                keyCount += 1
        if keyCount < k and result[j]:
            isAns = False
            break
        if keyCount >= k and result[j] is False:
            isAns = False
            break
    if isAns:
        ans += 1

print(ans)
