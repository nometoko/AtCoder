n = int(input())
div = int(1e9 + 7)

first = 1
second = 1
for i in range(3, n + 1):
    tmp = (first + second) % div
    first = second
    second = tmp

print(second)
