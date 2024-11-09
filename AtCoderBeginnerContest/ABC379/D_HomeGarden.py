from collections import deque

q = int(input())

que = deque()
now = 0
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        que.append(now)
    elif query[0] == 2:
        now += query[1]
    elif query[0] == 3:
        threshold = now - query[1]
        count = 0
        while que and que[0] <= threshold:
            que.popleft()
            count += 1
        print(count)
