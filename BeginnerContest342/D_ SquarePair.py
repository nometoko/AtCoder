n = int(input())
a = list(map(int, input().split()))
square = dict()
for i in range(n):
    if a[i] == 0:
        if 0 in square:
            square[0] += 1
        else:
            square[0] = 1
        continue

    for j in reversed(range(1, int(a[i] ** 0.5) + 1)):
        if a[i] % (j ** 2) == 0:
            if a[i] // (j ** 2) in square:
                square[a[i] // (j ** 2)] += 1
            else:
                square[a[i] // (j ** 2)] = 1
            break
ans = 0

if 0 in square:
    tmp = square[0]
    if tmp > 0:
        ans += (n - 1 + n - tmp) * tmp // 2
    square.pop(0)

for i in square.values():
    ans += i * (i - 1) // 2

print(ans)
