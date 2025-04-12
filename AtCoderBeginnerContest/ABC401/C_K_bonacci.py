from collections import deque

n, k = map(int, input().split())

if n < k:
  print(1)
  exit()

sum = k
q = deque([1] * k)
for i in range(k, n + 1):
  q.append(sum)
  sum = int(((sum % 1e9) * 2) % 1e9)
  sum -= q.popleft()
  sum = int(sum % 1e9)

print(q.pop())
