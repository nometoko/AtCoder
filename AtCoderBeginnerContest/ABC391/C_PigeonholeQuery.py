n, q = map(int, input().split())

nest = [1] * n
bird = [i for i in range(n)]
ans = 0

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a, b = query[1] - 1, query[2] - 1
        preBird = bird[a]
        bird[a] = b
        nest[preBird] -= 1
        nest[b] += 1
        if nest[preBird] == 1:
            ans -= 1
        if nest[b] == 2:
            ans += 1

    else:
        print(ans)
