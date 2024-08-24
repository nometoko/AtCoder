n = int(input())
a = list(map(int, input().split()))

fromLeft = a.copy()
fromRight = a.copy()

for i in range(1, n):
    fromLeft[i] = max(fromLeft[i - 1], a[i])
    j = n - i - 1
    fromRight[j] = max(fromRight[j + 1], a[j])

d = int(input())
for _ in range(d):
    left, right = map(int, input().split())
    if left == 1:
        print(fromRight[right])
    elif right == n:
        print(fromLeft[left - 2])
    else:
        print(max(fromLeft[left - 2], fromRight[right]))
