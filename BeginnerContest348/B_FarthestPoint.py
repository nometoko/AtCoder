import numpy as np

n = int(input())
x = []
for i in range(n):
    x.append(np.array(list(map(int, input().split()))))

distance = [[0] * (n - 1) for _ in range(n)]
for i in range(n):
    for j in range(i):
        distance[i][j] = distance[j][i - 1]

    for j in range(i + 1, n):
        distance[i][j - 1] = np.linalg.norm(x[i] - x[j])


for i in range(len(distance)):
    ans = distance[i].index(max(distance[i]))
    if ans < i:
        print(ans + 1)
    else:
        print(ans + 2)
