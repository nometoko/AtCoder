n, q = map(int, input().split())

a = [i for i in range(1, n + 1)]
top_ind = 0

for _ in range(q):
    query = list(map(int, input().split()))

    q_type = query[0]

    if q_type == 1:
        p, x = query[1] - 1, query[2]
        a[(p + top_ind) % n] = x

    elif q_type == 2:
        p = query[1] - 1
        print(a[(p + top_ind) % n])

    else:
        k = query[1]
        top_ind += k
        top_ind %= n
