n = int(input())
a = list(map(int, input().split()))
sumA = [0] * n
sumA[0] = a[0]
minSumIndex = 0
for i in range(1, n):
    sumA[i] = sumA[i-1] + a[i]
    if sumA[i] < sumA[minSumIndex]:
        minSumIndex = i

if sumA[minSumIndex] < 0:
    print(sumA[-1] - sumA[minSumIndex])
else:
    print(sumA[-1])
