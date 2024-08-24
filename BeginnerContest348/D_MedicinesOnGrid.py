from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(start):
    distance = [[-1] * w for _ in range(h)]
    q = deque()
    q.append([start[0], start[1], 0])
    while q:
        x, y, dist = q.popleft()
        if distance[x][y] != -1:
            continue
        distance[x][y] = dist
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and gridMap[nx][ny] != '#' and distance[nx][ny] == -1:
                q.append([nx, ny, dist + 1])
    return distance

def bfs2(start, goal):
    q = deque()
    q.append(start)
    hist = set()
    while q:
        index = q.popleft()
        if index == goal:
            return True
        if index in hist:
            continue
        hist.add(index)
        for i in range(n):
            if graph[index][i] and i not in hist:
                q.append(i)
    return False



h, w = map(int, input().split())
gridMap = []
for i in range(h):
    row = input()
    if 'S' in row:
        start = [i, row.index('S')]
    if 'T' in row:
        goal = [i, row.index('T')]
    gridMap.append(row)

n = int(input())
medicine = [[0] * w for _ in range(h)]
med_list = []
for i in range(n):
    r, c, e = map(int, input().split())
    medicine[r - 1][c - 1] = e
    med_list.append([r - 1, c - 1, e])
    if (r - 1, c - 1) == (start[0], start[1]):
        start_ind = i
    elif (r - 1, c - 1) == (goal[0], goal[1]):
        goal_ind = i

if medicine[start[0]][start[1]] == 0:
    print('No')
else:
    if medicine[goal[0]][goal[1]] == 0:
        medicine[goal[0]][goal[1]] = 1
        med_list.append([goal[0], goal[1], 1])
        n += 1
        goal_ind = n - 1

    graph = [[False] * n for _ in range(n)]
    for i in range(n):
        distance = bfs([med_list[i][0], med_list[i][1]])
        for j in range(n):
            if i == j:
                continue
            if distance[med_list[j][0]][med_list[j][1]] != -1 and distance[med_list[j][0]][med_list[j][1]] <= med_list[i][2]:
                graph[i][j] = True

    if bfs2(start_ind, goal_ind):
        print('Yes')
    else:
        print('No')
