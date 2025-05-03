n, m = map(int, input().split())

if n != m:
  print('No')
  exit()

graph = dict()

for _ in range(n):
  a, b = map(int, input().split())
  if a not in graph:
    graph[a] = set()
  if b not in graph:
    graph[b] = set()
  graph[a].add(b)
  graph[b].add(a)


visited = set()
start = 1
node = start
for i in range(m):
  try:
    next_node = graph[node].pop()
    graph[next_node].remove(node)
    # print(next_node, visited)
    if next_node in visited:
      print('No')
      exit()
    visited.add(next_node)
    node = next_node

  except KeyError:
    print('No')
    exit()

if node == start:
  print('Yes')
else:
  print('No')
