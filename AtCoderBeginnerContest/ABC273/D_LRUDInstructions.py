import bisect
DEBUG = False

h, w, rs, ls = map(int, input().split())
n = int(input())
wall_row = dict()
wall_col = dict()

for i in range(n):
    x, y = map(int, input().split())
    if x not in wall_row:
        wall_row[x] = [y]
    else:
        wall_row[x].append(y)
    if y not in wall_col:
        wall_col[y] = [x]
    else:
        wall_col[y].append(x)

pos = [rs, ls]
for i, j in wall_row.items():
    j.sort()
for i, j in wall_col.items():
    j.sort()

if DEBUG:
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if i in wall_row and j in wall_col:
                if j in wall_col and i in wall_col[j]:
                    print('#', end='')
                else:
                    print('.', end='')
            else:
                print('.', end='')
    print()

q = int(input())
for _ in range(q):
    d, l = map(str, input().split())
    # print(pos, d, l)
    l = int(l)
    if d == 'U' or d == 'D':
        if pos[1] not in wall_col:
            if d == 'U':
                pos[0] = max(1, pos[0] - l)
            else:
                pos[0] = min(h, pos[0] + l)
        else:
            if d == 'U':
                idx = bisect.bisect_left(wall_col[pos[1]], pos[0])
                idx_new = bisect.bisect_left(wall_col[pos[1]], pos[0] - l)
                if idx_new != idx:
                    pos[0] = wall_col[pos[1]][idx - 1] + 1
                else:
                    pos[0] = max(1, pos[0] - l)
            else:
                idx = bisect.bisect_right(wall_col[pos[1]], pos[0])
                idx_new = bisect.bisect_right(wall_col[pos[1]], pos[0] + l)
                if idx_new != idx:
                    pos[0] = wall_col[pos[1]][idx] - 1
                else:
                    pos[0] = min(h, pos[0] + l)
    else:
        if pos[0] not in wall_row:
            if d == 'L':
                pos[1] = max(1, pos[1] - l)
            else:
                pos[1] = min(w, pos[1] + l)
        else:
            if d == 'L':
                idx = bisect.bisect_left(wall_row[pos[0]], pos[1])
                idx_new = bisect.bisect_left(wall_row[pos[0]], pos[1] - l)
                if idx_new != idx:
                    pos[1] = wall_row[pos[0]][idx - 1] + 1
                else:
                    pos[1] = max(1, pos[1] - l)
            else:
                idx = bisect.bisect_right(wall_row[pos[0]], pos[1])
                idx_new = bisect.bisect_right(wall_row[pos[0]], pos[1] + l)
                if idx_new != idx:
                    pos[1] = wall_row[pos[0]][idx] - 1
                else:
                    pos[1] = min(w, pos[1] + l)
    print(pos[0], pos[1])
