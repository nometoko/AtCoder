n, t = map(int, input().split())

m = dict()
scores = [0] * n
m[0] = n

for i in range(t):
    a, b = map(int, input().split())
    m[scores[a - 1]] -= 1
    if m[scores[a - 1]] == 0:
        m.pop(scores[a - 1])
    scores[a - 1] += b
    if scores[a - 1] not in m:
        m[scores[a - 1]] = 0
    m[scores[a - 1]] += 1
    print(len(m))
