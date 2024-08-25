import numpy as np

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

ans = 0
while True:
    count = 0
    for i in range(min(4, len(a))):
        if a[i] > 0:
            count += 1
    if count <= 1:
        break
    a[0] -= 1
    a[1] -= 1
    a.sort(reverse=True)
    ans += 1

print(ans)
