n = int(input())
s = input()
c = list(map(int, input().split()))

ans = 0
tmp = [[] for _ in range(2)]
if s[0] == '0':
    ans += c[0]
# print('1', end='')
for i in range(1, n):
    # print(i % 2, end='')
    if s[i] == str(1 - i % 2):
        ans += c[i]
tmp[0].append(ans)
tmp[1].append(sum(c) - ans)
# print()
for j in range(1, n - 1):
    if s[j] == str('1'):
        tmp[0].append(tmp[1][j - 1] - c[j])
        tmp[1].append(tmp[0][j - 1] + c[j])
    else:
        tmp[0].append(tmp[1][j - 1] + c[j])
        tmp[1].append(tmp[0][j - 1] - c[j])
# print(*tmp, sep=' ')
print(min(min(tmp[0]), min(tmp[1])), end='')
