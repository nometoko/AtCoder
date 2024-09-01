h, w = map(int, input().split())

grid = [list(input()) for _ in range(h)]

for i in range(w):
    print([grid[j][i] for j in range(h)].count('#'), end=' ')

print()
