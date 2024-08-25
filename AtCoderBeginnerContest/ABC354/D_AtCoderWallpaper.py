x1, y1, x2, y2 = map(int, input().split())

x_period = (x2 - x1) // 4
y_period = (y2 - y1) // 2
# print(x_period, y_period)
ans = x_period * y_period * 8
if y1 + y_period * 2 != y2:
        ans += x_period * 4
for x in range(x1 + x_period * 4, x2):
    if x % 4 == 0 or x % 4 == 1:
        ans += 3 * y_period
    else:
        ans += 1 * y_period
    # print(x, y1, ans)
    for y in range(y1 + 2 * y_period, y2):
        if x % 4 == 0:
            if y % 2 == 0:
                ans += 2
            else:
                ans += 1
        elif x % 4 == 1:
            if y % 2 == 0:
                ans += 1
            else:
                ans += 2
        elif x % 4 == 2:
            if y % 2 == 0:
                ans += 0
            else:
                ans += 1
        elif x % 4 == 3:
            if y % 2 == 0:
                ans += 1
            else:
                ans += 0
        # print(x, y, ans)
print(ans)
