n, m = map(int, input().split())
pare = [[-1, 1] for _ in range(n + 1)]


def get_root(i, pare) -> int:
    while pare[i][0] != -1:
        i = pare[i][0]
    return i


# keyのほうが小さい
path_smaller = dict()
# keyのほうが大きい
path_bigger = dict()


for _ in range(m):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    if u not in path_smaller:
        path_smaller[u] = set()

    path_smaller[u].add(v)

    if v not in path_bigger:
        path_bigger[v] = set()
    path_bigger[v].add(u)


delete = set()

# union木
for i in range(1, n + 1):
    if i in delete:
        delete.remove(i)

    if i in path_bigger:
        for neighbour in path_bigger[i]:
            root_i = get_root(i, pare)
            root_neibour = get_root(neighbour, pare)
            if root_i != root_neibour:
                if pare[root_i][1] > pare[root_neibour][1]:
                    root_i, root_neibour = root_neibour, root_i

                pare[root_i][0] = root_neibour
                pare[root_neibour][1] += pare[root_i][1]

    if i in path_smaller:
        for neighbour in path_smaller[i]:
            delete.add(neighbour)

    root_i = get_root(1, pare)
    if pare[root_i][1] != i:
        print(-1)
    else:
        print(len(delete))
