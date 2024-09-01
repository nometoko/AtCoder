from collections import deque

n = int(input())

ladders = dict()
for i in range(n):
    a, b = map(int, input().split())
    if a in ladders:
        ladders[a].add(b)
    else:
        ladders[a] = set([b])
    if b in ladders:
        ladders[b].add(a)
    else:
        ladders[b] = set([a])

hist = set()
now = 1
highest = 1
visit = deque([1])

while visit:
    now = visit.popleft()
    if now in hist:
        continue
    highest = max(highest, now)
    hist.add(now)
    if now in ladders:
        for next in ladders[now]:
            if next not in hist:
                visit.append(next)

print(highest)
