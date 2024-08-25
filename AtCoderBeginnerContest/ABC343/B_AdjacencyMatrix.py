n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] == 1:
            print(i + 1, end=' ')
    print()
