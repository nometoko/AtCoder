from collections import deque
n, q = map(int, input().split())

pos = [[i + 1, 0] for i in range(n - 1, -1, -1)]

for _ in range(q):
    a, b = input().split()
    a = int(a)
    if a == 2:
        b = int(b)
        print(*pos[-b])
    else:
        newTop = pos[-1].copy()
        if b == 'U':
            newTop[1] += 1
            pos.append(newTop)
        elif b == 'D':
            newTop[1] -= 1
            pos.append(newTop)
        elif b == 'L':
            newTop[0] -= 1
            pos.append(newTop)
        else:
            newTop[0] += 1
            pos.append(newTop)
        # print(pos)
