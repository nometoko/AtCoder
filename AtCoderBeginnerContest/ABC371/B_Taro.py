n, m = map(int, input().split())

born = [False] * n

for i in range(m):
  a, b = input().split()
  a = int(a)
  if born[a - 1] is False and b == 'M':
    print('Yes')
    born[a - 1] = True
  else:
    print('No')
