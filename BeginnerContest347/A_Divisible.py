n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = []

for i in range(n):
    if arr[i] % k == 0:
        print(int(arr[i] / k), end=" ")

