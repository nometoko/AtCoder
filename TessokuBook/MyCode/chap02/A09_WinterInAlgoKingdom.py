h, w, n = map(int, input().split())
mapping = [[0] * (w + 2) for _ in range(h + 2)]

for i in range(n):
    a, b, c, d = map(int, input().split())
    mapping[a][b] += 1
    mapping[a][d + 1] -= 1
    mapping[c + 1][b] -= 1
    mapping[c + 1][d + 1] += 1

for i in range(1, h + 1):
    for j in range(1, w + 1):
        mapping[i][j] = mapping[i][j - 1] + mapping[i][j]

for j in range(1, w + 1):
    for i in range(1, h + 1):
        mapping[i][j] = mapping[i - 1][j] + mapping[i][j]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        print(mapping[i][j], end=" ")
    print()
