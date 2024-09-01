# the way to solve from answer

n, x, y = map(int, input().split())
a = list(map(int, input().split()))
a_x = [a[2 * i] for i in range((n + 1) // 2)]
a_y = [a[2 * i + 1] for i in range(n // 2)]


sum_a_x = sum(a_x)
sum_a_y = sum(a_y)
if abs(x) > abs(sum_a_x) or abs(y) > abs(sum_a_y):
    print('No')
    exit()
dp_x = [False] * (sum_a_x * 2 + 1)
dp_y = [False] * (sum_a_y * 2 + 1)

dp_x[sum_a_x + a[0]] = True
dp_y[sum_a_y] = True

for i in range(1, len(a_x)):
    true_ind = [False] * (sum_a_x * 2 + 1)
    for j in range(sum_a_x * 2 + 1):
        if dp_x[j]:
            true_ind[j + a_x[i]] = True
            true_ind[j - a_x[i]] = True
    dp_x = true_ind

for i in range(len(a_y)):
    true_ind = [False] * (sum_a_y * 2 + 1)
    for j in range(sum_a_y * 2 + 1):
        if dp_y[j]:
            true_ind[j + a_y[i]] = True
            true_ind[j - a_y[i]] = True
    dp_y = true_ind

# for i, x in enumerate(dp_x):
    # print([i - sum_a_x, x], end=' ')
# print()
# for i, y in enumerate(dp_y):
    # print([i - sum_a_y, y], end=' ')
# print()
if dp_x[sum_a_x + x] and dp_y[sum_a_y + y]:
    print('Yes')
else:
    print('No')
