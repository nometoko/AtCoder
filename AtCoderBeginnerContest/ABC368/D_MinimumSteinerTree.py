import bisect

n, k = map(int, input().split())
ans = n
connect = [set() for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    connect[a].add(b)
    connect[b].add(a)

v = list(map(int, input().split()))
v.sort()
ans = n

if k == 1:
    print(1)
else:
    leaf = []
    for i, c in enumerate(connect):
        if len(c) == 1:
            leaf.append(i)

    for node in leaf:
        index = bisect.bisect_left(v, node + 1)
        if index >= k or v[index] != node + 1:
            ans -= 1
            neighbor = connect[node].pop()
            connect[neighbor].remove(node)
            # print('remove', node + 1)
            if len(connect[neighbor]) == 1:
                leaf.append(neighbor)
            
    print(ans)
