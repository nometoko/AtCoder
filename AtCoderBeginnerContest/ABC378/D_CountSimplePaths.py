import itertools

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def count_path(pos, k, history=set()):
    if k == 0:
        return 1
    history.add(pos)
    count = 0
    for direction in move:
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if next_pos[0] < 0 or next_pos[0] >= h or next_pos[1] < 0 or next_pos[1] >= w:
            continue
        if grid[next_pos[0]][next_pos[1]] == '#':
            continue
        if next_pos in history:
            continue
        count += count_path(next_pos, k - 1, history.copy())
    return count

h, w, k = map(int, input().split())
grid = []

for _ in range(h):
    grid.append(input())

ans = 0
for col, row in itertools.product(range(h), range(w)):
    if grid[col][row] == '#':
        continue
    ans += count_path((col, row), k, set())
print(ans)
