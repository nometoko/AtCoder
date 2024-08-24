import itertools

n, k = map(int, input().split())
a = list(map(int, input().split()))

# aを半分に分けて作れる数を管理
half = len(a)//2

left = set()
# ２進数で選ぶか選ばないか管理
for i in range(2 ** half):
    strBin = str(bin(i))[2:]
    tmp = 0
    for j in range(half):
        if j < len(strBin) and strBin[len(strBin) - j - 1] == '1':
            tmp += a[j]
    left.add(tmp)

right = set()
for i in range(2 ** (n - half)):
    strBin = str(bin(i))[2:]
    tmp = 0
    for j in range(n - half):
        if j < len(strBin) and strBin[len(strBin) - j - 1] == '1':
            tmp += a[half + j]
    right.add(tmp)

isYes = False
for i in left:
    if k - i in right:
        isYes = True
        break

# print(left)
# print(right)
if isYes:
    print('Yes')
else:
    print('No')
