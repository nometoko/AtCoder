from collections import deque

def bfs(start, follow):
    q = deque()
    q.append(start)
    connected = set()
    while q:
        now = q.popleft()
        if now in connected:
            continue
        connected.add(now)
        for i in follow[now]:
            if i not in connected:
                q.append(i)
    return connected

n, m = map(int, input().split())
follow = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    follow[a - 1].append(b - 1)
    follow[b - 1].append(a - 1)

ans = 0
searched = [False] * n
for i in range(n):
    if not searched[i]:
        new_connected = bfs(i, follow)
        len_new_connected = len(new_connected)
        already_connected = 0
        for j in new_connected:
            searched[j] = True
            already_connected += len(follow[j])
        already_connected //= 2
        ans += len_new_connected * (len_new_connected - 1) // 2 - already_connected

print(ans)
