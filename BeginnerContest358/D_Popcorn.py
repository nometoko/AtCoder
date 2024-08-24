import collections

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

a = collections.deque(a)
b = collections.deque(b)

ans = 0
b_index = 0
while a and b_index < m:
    a_i = a.popleft()
    if a_i >= b[b_index]:
        ans += a_i
        b_index += 1
    
if b_index < m:
    print(-1)
else:
    print(ans)