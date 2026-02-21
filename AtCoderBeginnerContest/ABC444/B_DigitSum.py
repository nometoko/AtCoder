n, k = map(int, input().split())

cnt = 0
for i in range(1, n + 1):
    digit_sum = 0
    while i > 0:
        digit_sum += i % 10
        i //= 10

    if digit_sum == k:
        cnt += 1
print(cnt)
