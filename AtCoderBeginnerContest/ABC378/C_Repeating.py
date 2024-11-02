n = int(input())
a = list(map(int, input().split()))
dictA = {}
for i, tmpA in enumerate(a):
    if tmpA not in dictA:
        print(-1, end=' ')
    else:
        print(dictA[tmpA], end=' ')
    dictA[tmpA] = i + 1
print()
