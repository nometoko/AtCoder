from collections import deque

h, w, k = map(int, input().split())

ans = float('inf')
s = []
for i in range(h):
    tmp = input()
    s.append(tmp)

if w >= k:
    for i in range(h):
        dot_count = [0] * w
        x_count = [0] * w
        for j in range(w):
            if j == 0:
                dot_count[j] = 0
                x_count[j] = 0
            else:
                dot_count[j] = dot_count[j - 1]
                x_count[j] = x_count[j - 1]
            if s[i][j] == '.':
                dot_count[j] += 1
            elif s[i][j] == 'x':
                x_count[j] += 1
        x_count = [0] + x_count
        dot_count = [0] + dot_count
        for j in range(w - k + 1):
            if x_count[j + k] - x_count[j] == 0:
                ans = min(ans, dot_count[j + k] - dot_count[j])

if h >= k:
    for i in range(w):
        dot_count = [0] * h
        x_count = [0] * h
        for j in range(h):
            if j == 0:
                dot_count[j] = 0
                x_count[j] = 0
            else:
                dot_count[j] = dot_count[j - 1]
                x_count[j] = x_count[j - 1]
            if s[j][i] == '.':
                dot_count[j] += 1
            elif s[j][i] == 'x':
                x_count[j] += 1
        x_count = [0] + x_count
        dot_count = [0] + dot_count
        for j in range(h - k + 1):
            if x_count[j + k] - x_count[j] == 0:
                ans = min(ans, dot_count[j + k] - dot_count[j])

if ans == float('inf'):
    print(-1)
else:
    print(ans)
