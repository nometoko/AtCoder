
n, q = map(int,input().split())
con = dict()

for _ in range(q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 1:
        if a not in con:
            con[a] = set([b])
        else:
            con[a].add(b)
    elif t == 2:
        if a in con:
            con[a].discard(b)
    else:
        if a in con and b in con and b in con[a] and a in con[b]:
                print("Yes")
        else:
            print("No")
