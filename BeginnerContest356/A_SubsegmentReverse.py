n, l, r = map(int, input().split())
for i in range(1, l):
    print(i, end=' ')
for i in range(r, l - 1, -1):
    print(i, end=' ')
for i in range(r + 1, n + 1):
    print(i, end=' ')
