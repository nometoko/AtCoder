n, m = map(int, input().split())

badCell = set()

move = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

knight = list()
for _ in range(m):
    x, y = map(int, input().split())
    knight.append((x, y))

for i in range(m):
    x, y = knight[i]
    for dx, dy in move:
        if 1 <= x + dx <= n and 1 <= y + dy <= n:
            badCell.add((x + dx, y + dy))

for i in range(m):
    badCell.add(knight[i])

print(n**2 - len(badCell))
