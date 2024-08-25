k = int(input())


def SierpinskiCarpet(n):
    if n == 0:
        return '#'
    before = SierpinskiCarpet(n-1)
    ans = ['' for _ in range(3 ** n)]
    for i in range(3):
        for j in range(len(before)):
            if i == 1:
                ans[3 ** (n - 1) * i + j] = before[j] + '.' * 3 ** (n - 1) + before[j]
            else:
                ans[3 ** (n - 1) * i + j] = before[j] * 3
    return ans

ans = SierpinskiCarpet(k)
for string in ans:
    print(string)
