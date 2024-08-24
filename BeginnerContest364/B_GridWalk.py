h, w = map(int, input().split())
pos = list(map(int, input().split()))

mapp = []
for i in range(h):
    mapp.append(input())
x = input()

for i in x:
    if i == 'U':
        if pos[0] != 1 and mapp[pos[0] - 2][pos[1] - 1] != '#':
            pos[0] -= 1
    elif i == 'D':
        if pos[0] != h and mapp[pos[0]][pos[1] - 1] != '#':
            pos[0] += 1
    elif i == 'L':
        if pos[1] != 1 and mapp[pos[0] - 1][pos[1] - 2] != '#':
            pos[1] -= 1
    elif i == 'R':
        if pos[1] != w and mapp[pos[0] - 1][pos[1]] != '#':
            pos[1] += 1

print(pos[0], pos[1])
