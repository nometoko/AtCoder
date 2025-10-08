from collections import deque

h, w = map(int, input().split())

grid = [input() for _ in range(h)]

# set -1 as initial value
grid_dist = [[-1] * w for _ in range(h)]

total_cnt = 0
que = deque()
for y in range(h):
    for x in range(w):
        if grid[y][x] == "#":
            que.append((x, y, 0))
            grid_dist[y][x] = 0
            total_cnt += 1

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while que:
    i, j, cnt = que.popleft()

    for dx, dy in move:
        new_x = i + dx
        new_y = j + dy

        # out of index
        if (new_x < 0 or w <= new_x) or (new_y < 0 or h <= new_y):
            continue

        # skip if already searched
        if grid_dist[new_y][new_x] != -1:
            continue

        # print(f"({i}, {j}) -> ({new_x}, {new_y})")

        black_cnt = 0
        for new_dx, new_dy in move:
            neighbour_x = new_x + new_dx
            neighbour_y = new_y + new_dy

            if (neighbour_x < 0 or w <= neighbour_x) or (
                neighbour_y < 0 or h <= neighbour_y
            ):
                continue

            if grid_dist[neighbour_y][neighbour_x] == cnt:
                black_cnt += 1

        # cannot fill black
        if black_cnt > 1:
            grid_dist[new_y][new_x] = -2

        else:
            grid_dist[new_y][new_x] = cnt + 1
            total_cnt += 1
            que.append((new_x, new_y, cnt + 1))

print(total_cnt)
