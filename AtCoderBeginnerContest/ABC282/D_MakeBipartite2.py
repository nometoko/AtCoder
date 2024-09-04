from collections import deque

n, m  = map(int, input().split())

graph = dict()
for _ in range(m):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = set([v])
    else:
        graph[u].add(v)
    if v not in graph:
        graph[v] = set([u])
    else:
        graph[v].add(u)

searched = set()
connected = []
bw = [-1] * n

for i in range(1, n + 1):
    if i not in searched:
        connected.append(set())
        bw[i - 1] = 0
        if i not in graph:
            searched.add(i)
            connected[-1].add(i)
            continue
        q = deque([i])
        while q:
            node = q.popleft()
            if node in searched:
                continue
            connected[-1].add(node)
            searched.add(node)
            for neighbor in graph[node]:
                if neighbor not in searched:
                    q.append(neighbor)
                    
                if bw[neighbor - 1] == -1:
                    bw[neighbor - 1] = 1 - bw[node - 1]
                else:
                    if bw[neighbor - 1] == bw[node - 1]:
                        print(0)
                        exit()

# print(connected)
# print(bw)
ans = n * (n - 1) // 2
# print(ans)
for group in connected:
    b_count = 0
    w_count = 0
    for node in group:
        if bw[node - 1] == 0:
            b_count += 1
        else:
            w_count += 1
    ans -= (b_count * (b_count - 1) // 2 + w_count * (w_count - 1) // 2)
    # print(ans)
ans -= m
print(ans)
