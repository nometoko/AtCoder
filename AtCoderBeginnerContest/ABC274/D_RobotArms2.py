from functools import cache

@cache
def dfs_x(ind, point):
    if ind == len(a_x):
        if point == x:
            return True
        else:
            return False
    if abs(point - x) > a_x_sum[-1] - a_x_sum[ind]:
        return False
    if dfs_x(ind + 1, point + a_x[ind]):
        return True
    if dfs_x(ind + 1, point - a_x[ind]):
        return True
    return False

@cache
def dfs_y(ind, point):
    if ind == len(a_y):
        if point == y:
            return True
        else:
            return False
    if abs(point - y) > a_y_sum[-1] - a_y_sum[ind]:
        return False
    if dfs_y(ind + 1, point + a_y[ind]):
        return True
    if dfs_y(ind + 1, point - a_y[ind]):
        return True
    return False

n, x, y = map(int, input().split())
a = list(map(int, input().split()))
a_x = [a[2 * i] for i in range((n + 1) // 2)]
a_y = [a[2 * i + 1] for i in range(n // 2)]
a_x_sum = [0] * (len(a_x) + 1)
a_y_sum = [0] * (len(a_y) + 1)
for i in range(len(a_x)):
    a_x_sum[i + 1] = a_x_sum[i] + a_x[i]
for i in range(len(a_y)):
    a_y_sum[i + 1] = a_y_sum[i] + a_y[i]

if dfs_x(1, a[0]) and dfs_y(0, 0):
    print('Yes')
else:
    print('No')
