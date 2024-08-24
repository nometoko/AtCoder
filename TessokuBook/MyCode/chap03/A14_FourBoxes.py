import itertools

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

ab = set()
cd = set()
for i, j in itertools.product(range(n), range(n)):
    ab.add(a[i] + b[j])
    cd.add(c[i] + d[j])

# print(ab, cd)
isYes = False
for i in ab:
    if k - i in cd:
        isYes = True
        break

if isYes:
    print('Yes')
else:
    print('No')
