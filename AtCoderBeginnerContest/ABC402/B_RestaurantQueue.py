from collections import deque

q = int(input())

que = deque()

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        que.append(query[1])
    else:
        print(que.popleft())
