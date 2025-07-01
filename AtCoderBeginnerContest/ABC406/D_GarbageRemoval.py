h, w, n = map(int, input().split())

gabage_x = dict()
gabage_y = dict()
for _ in range(n):
    x, y = map(int, input().split())

    if x not in gabage_x:
        gabage_x[x] = set()
    gabage_x[x].add(y)

    if y not in gabage_y:
        gabage_y[y] = set()
    gabage_y[y].add(x)

q = int(input())
for _ in range(q):
    query, xy = map(int, input().split())

    if query == 1:
        if xy in gabage_x:
            print(len(gabage_x[xy]))
            for y in gabage_x[xy]:
                gabage_y[y].discard(xy)
            gabage_x[xy].clear()
        else:
            print(0)

    else:
        if xy in gabage_y:
            print(len(gabage_y[xy]))
            for x in gabage_y[xy]:
                gabage_x[x].discard(xy)
            gabage_y[xy].clear()
        else:
            print(0)
