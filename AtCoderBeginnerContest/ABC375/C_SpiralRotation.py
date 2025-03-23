# numpy配列を使わずに回転したらめっちゃ早くなった

def rot(a, i, j, rot_num):
    if rot_num == 0:
        # print(f"({i},{j})", end=' ')
        return a[i][j]
    elif rot_num == 1:
        # print(f"({n - j - 1},{i})", end=' ')
        return a[n - j - 1][i]
    elif rot_num == 2:
        # print(f"({n - i - 1},{n - j - 1})", end=' ')
        return a[n - i - 1][n - j - 1]
    elif rot_num == 3:
        # print(f"({j},{n - i - 1})", end=' ')
        return a[j][n - i - 1]

n = int(input())

new_a = [['' for _ in range(n)] for _ in range(n)]

a = []
for i in range(n):
    a.append(list(input()))

for i in range(n):
    for j in range(n):
        rot_a = (min(i, j, n - i - 1, n - j - 1) + 1) % 4
        new_a[i][j] = rot(a, i, j, rot_a)

for row in new_a:
    print(''.join(row), end='\n')

# a[0, 1] → a[n - 1 - 1, 0] → a[n - 1 - 0, n - 1 - 1] → a[1, n - 1 - 0]

