n, q = map(int, input().split())
a = list(map(int, input().split()))
totalA = [0]
for i in range(n):
    totalA.append(totalA[i] + a[i])
# print(*totalA)
for i in range(q):
    left, right = map(int, input().split())
    print(totalA[right] - totalA[left - 1])
