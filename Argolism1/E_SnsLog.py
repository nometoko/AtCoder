n, q = map(int, input().split())
s = []
follow = [[0] * n for _ in range(n)]

for _ in range(q):
    s.append(list(map(int, input().split())))

for i in s:
    pos = i[1] - 1
    if i[0] == 1:
        follow[pos][i[2] - 1] = 1
        continue

    elif i[0] == 2:
        for j in range(n):
            if follow[j][pos] and j != pos:
                follow[pos][j] = 1
        continue

    elif i[0] == 3:
        tmp = follow[pos].copy()
        for j in range(n):
            if tmp[j]:
                for k in range(n):
                    if follow[j][k] and k != pos:
                        follow[pos][k] = 1
        continue

for i in follow:
    for j in i:
        if j == 1:
            print("Y", end="")
        else:
            print("N", end="")
    print()
