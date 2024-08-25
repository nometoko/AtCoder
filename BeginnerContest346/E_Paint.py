h, w, m = map(int, input().split())

# 2次元配列の初期化
ans = dict()
tax = []
for i in range(m):
    tax.append(list(map(int, input().split())))

tax = reversed(tax)
rows = [False] * h
cols = [False] * w
row_True = 0
col_True = 0
for t, a, x in tax:
    a -= 1
    if x not in ans:
        ans[x] = 0
    if t == 1:
        if rows[a] is False:
            rows[a] = True
            row_True += 1
            ans[x] += w - col_True
    else:
        if cols[a] is False:
            cols[a] = True
            col_True += 1
            ans[x] += h - row_True
    if ans[x] == 0:
        ans.pop(x, None)

if len(ans) == 0:
    print(1)
    print(0, h * w)
else:
    ans.pop(0, None)
    ans = sorted(ans.items(), key=lambda x: x[0])
    sum = 0
    k = 0
    for color, num in ans:
        k += 1
        sum += num

    if h * w - sum > 0:
        print(k + 1)
        print(0, h * w - sum)
    else:
        print(k)

    for color, num in ans:
        print(color, num)

