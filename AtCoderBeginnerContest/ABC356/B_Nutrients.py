n, m = map(int, input().split())
a = list(map(int, input().split()))
nutrition = [0] * m
for _ in range(n):
    x = list(map(int, input().split()))
    for i in range(m):
        nutrition[i] += x[i]

for i in range(m):
    if nutrition[i] < a[i]:
        print('No')
        exit(0)
print('Yes')
