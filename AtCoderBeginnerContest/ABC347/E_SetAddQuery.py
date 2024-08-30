n, q = map(int, input().split())
x = list(map(int, input().split()))
inout = [-1] * n
ans = [0] * n
sum_len_s = [0] * q
len_s = 0

len_s = 1
sum_len_s[0] = 1
inout[x[0] - 1] = 0

for ind, query in enumerate(x):
    if ind == 0:
        continue
    if inout[query - 1] == -1:
        inout[query - 1] = sum_len_s[ind - 1]
        len_s += 1
    else:
        added = inout[query - 1]
        ans[query - 1] = ans[query - 1] + sum_len_s[ind - 1] - added
        inout[query - 1] = -1
        len_s -= 1

    sum_len_s[ind] = sum_len_s[ind - 1] + len_s
for i, an in enumerate(inout):
    if an != -1:
        ans[i] = ans[i] + sum_len_s[-1] - an

print(*ans)
