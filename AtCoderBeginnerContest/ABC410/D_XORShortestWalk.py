from collections import deque


def xor(x, y):
    return x ^ y


n, m = map(int, input().split())

paths = {}

for _ in range(m):
    a, b, w = map(int, input().split())

    a -= 1
    b -= 1

    if a not in paths:
        paths[a] = []
    paths[a].append((b, w))

# print(paths)

dp = [[0] * (2**10) for _ in range(n)]

q = deque([(0, 0)])

while q:
    (pos, score) = q.popleft()
    for next, weight in paths.get(pos, []):
        new_score = xor(score, weight)

        if dp[next][new_score] == 0:
            dp[next][new_score] = 1
            q.append((next, new_score))

# print(dp)
for i in range(2**10):
    if dp[-1][i] == 1:
        print(i)
        exit()

print(-1)
