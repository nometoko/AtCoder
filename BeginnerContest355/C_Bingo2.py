n, t = map(int, input().split())
a = list(map(int, input().split()))

column = [0] * n
row = [0] * n
diagonal_1 = [0] * n
diagonal_2 = [0] * n

for i in range(t):
    num = a[i]
    num -= 1
    column[num % n] += 1
    row[num // n] += 1
    if num % n == num // n:
        diagonal_1[num % n] += 1
    if num % n + num // n == n - 1:
        diagonal_2[num % n] += 1

    for j in range(n):
        if column[j] == n or row[j] == n:
            print(i + 1)
            exit(0)
    if 0 not in diagonal_1:
        print(i + 1)
        exit(0)
    if 0 not in diagonal_2:
        print(i + 1)
        exit(0)
print(-1)
