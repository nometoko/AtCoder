n = int(input())
a = list(map(int, input().split()))

top = set()
tail = set()
from_top = [0] * (n - 1)
from_tail = [0] * (n - 1)

for i in range(n - 1):
  top.add(a[i])
  tail.add(a[n - i - 1])

  from_top[i] = len(top)
  from_tail[n - i - 2] = len(tail)

# max
ans = 0
for i in range(n - 1):
  ans = max(ans, from_top[i] + from_tail[i])

print(ans)
