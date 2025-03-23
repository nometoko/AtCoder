from itertools import permutations

n = int(input())
mg = int(input())

g_graph = [[False] * n for _ in range(n)]
for _ in range(mg):
  a, b = map(int, input().split())
  g_graph[a - 1][b - 1] = True
  g_graph[b - 1][a - 1] = True

mh = int(input())
h_graph = [[False] * n for _ in range(n)]
for _ in range(mh):
  a, b = map(int, input().split())
  h_graph[a - 1][b - 1] = True
  h_graph[b - 1][a - 1] = True

cost = [[0] * n for _ in range(n)]

for i in range(n - 1):
  cost_input = list(map(int, input().split()))
  for idx, c in enumerate(cost_input):
    cost[i][idx + i + 1] = c
    cost[idx + i + 1][i] = c

# hを並び替える 8!通り
ori = [i for i in range(n)]

ans = float('inf')

for perm in permutations(ori):
  # print(perm)
  ans_tmp = 0
  for i in range(n):
    for j in range(i + 1, n):
      if g_graph[i][j] is h_graph[perm[i]][perm[j]]:
        continue
      else:
        ans_tmp += cost[perm[i]][perm[j]]

  # print(ans_tmp)
  ans = min(ans, ans_tmp)
  # if ans == ans_tmp:
    # print(ans, perm)

print(ans)

