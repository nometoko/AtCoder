n = int(input())
p = list(map(int, input().split()))
orderedP = sorted([p[i], i] for i in range(n))
q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    if orderedP[a - 1][1] < orderedP[b - 1][1]:
        print(a)
    else:
        print(b)
