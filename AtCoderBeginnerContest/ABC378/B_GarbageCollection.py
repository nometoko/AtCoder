n = int(input())

collection = []
for i in range(n):
    collection.append(list(map(int, input().split())))

q = int(input())
for i in range(q):
    t, d = map(int, input().split())
    q, r = collection[t-1]
    if d % q == r:
        cycle = d // q
    else:
        cycle = (d  - r) // q + 1
    print(cycle * q + r)
