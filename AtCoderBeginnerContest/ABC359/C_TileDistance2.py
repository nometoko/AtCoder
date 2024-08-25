sx, sy = map(int, input().split())
tx, ty = map(int, input().split())

diff_y = abs(sy - ty)
if sy % 2 == 1:
    if sx - tx > 0:
        if sx % 2 == 0:
            sx -= 1
        sx = max(tx, sx - diff_y)
    else:
        if sx % 2 == 1:
            sx += 1
        sx = min(tx, sx + diff_y)
else:
    if sx - tx > 0:
        if sx % 2 == 1:
            sx -= 1
        sx = max(tx, sx - diff_y)
    else:
        if sx % 2 == 0:
            sx += 1
        sx = min(tx, sx + diff_y)

if ty % 2 == 1:
    diff_x = abs((sx - 1) // 2 - (tx - 1) // 2)
else:
    diff_x = abs(sx // 2 - tx // 2)

# print(sx, diff_x)
print(diff_x + diff_y)
