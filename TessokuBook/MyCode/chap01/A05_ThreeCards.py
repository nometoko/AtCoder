n, k = map(int, input().split())
count = 0

for i in range(1, min(n + 1, k // 3 + 2)):
    for j in range(i, min(n + 1, (k // 3 + 2) * 2)):
        # print(i, j)
        tmp = k - i - j
        if tmp < j:
            break
        if tmp <= n:
            if i == j == tmp:
                count += 1
            elif i == j or i == tmp or j == tmp:
                count += 3
            else:
                count += 6

print(count)
