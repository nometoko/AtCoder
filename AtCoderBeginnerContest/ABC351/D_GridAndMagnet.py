from functools import cache
import sys
sys.setrecursionlimit(10 ** 7)

def checkMag(i, j):
    # Check if the current cell is next to a magnet
    # return True if it is, else False
    if 0 <= i - 1 and grid[i - 1][j] == '#':
        return True
    if i + 1 < h and grid[i + 1][j] == '#':
        return True
    if j - 1 >= 0 and grid[i][j - 1] == '#':
        return True
    if j + 1 < w and grid[i][j + 1] == '#':
        return True
    return False

def searchMap(i, j, area = 0):
    if Mag[i][j]:
        if (i, j) not in hist:
            hist.add((i, j))
            area += 1
    else:
        area += 1
        search[i][j] = True
        if 0 <= i - 1 and search[i - 1][j] is False:
            area = searchMap(i - 1, j, area)
        if i + 1 < h and search[i + 1][j] is False:
            area = searchMap(i + 1, j, area)
        if 0 <= j - 1 and search[i][j - 1] is False:
            area = searchMap(i, j - 1, area)
        if j + 1 < w and search[i][j + 1] is False:
            area = searchMap(i, j + 1, area)
    return area

if __name__ == '__main__':
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]
    search = [[False] * w for _ in range(h)]
    Mag = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '.' and checkMag(i, j):
                Mag[i][j] = True
    ans = 1
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '.' and Mag[i][j] is False and search[i][j] is False:
                hist = set()
                count = searchMap(i, j)
                ans = max(ans, count)
    print(ans)
