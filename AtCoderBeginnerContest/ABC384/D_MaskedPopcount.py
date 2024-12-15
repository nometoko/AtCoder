import bisect

DEBUG = False

n, s = map(int, input().split())
a = list(map(int, input().split()))

sumFromStart = [0] * (n + 1)
sumFromEnd = [0] * (n + 1)
sumFromStart[1] = a[0]
sumFromEnd[1] = a[n - 1]

for i in range(2, n + 1):
    sumFromStart[i] = sumFromStart[i - 1] + a[i - 1]
    sumFromEnd[i] = sumFromEnd[i - 1] + a[n - i]

sumA = sumFromStart[-1]
amari = s % sumA
if amari == 0:
    print('Yes')
    exit()

if DEBUG:
    print('amari:', amari)
    print(sumFromStart)
    print(sumFromEnd)
leftMax = bisect.bisect_right(sumFromStart, amari + sumA)
for leftIndex in range(leftMax):
    leftSum = sumFromStart[leftIndex]

    nokori = amari - leftSum
    if nokori < 0:
        nokori += sumA
    rightIndex = bisect.bisect_left(sumFromEnd, nokori)
    if DEBUG:
        print(leftSum, nokori, rightIndex)

    if sumFromEnd[rightIndex] == nokori:
        print('Yes')
        exit()

print('No')
