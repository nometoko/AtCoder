n, m = map(int, input().split())
ansList = []
for _ in range(n):
    s = input()
    ansList.append(s)

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        isClear = True
        for k in range(m):
            if ansList[i][k] == 'x' and ansList[j][k] == 'x':
                isClear = False
                break
        if isClear:
            ans += 1
print(ans)
