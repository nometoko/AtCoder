n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))

def check(x):
    cnt = 0
    pre = 0
    for i in range(n):
        if a[i] - pre >= x and l - a[i] >= x:
            cnt += 1
            pre = a[i]
    if l - pre >= x:
        cnt += 1
    if cnt >= k + 1:
        return True
    else:
        return False

left = -1
right = l + 1
while right - left > 1:
    mid = left + (right - left) // 2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)
