n, m = map(int, input().split())

pop = []
for i in range(n):
    pop.append(input())

ans = n
for i in range(2 ** n):
    i_bin = bin(i)[2:].zfill(n)
    taste = [False] * m
    for j in range(n):
        if i_bin[j] == '1':
            for k in range(m):
                if pop[j][k] == 'o' and not taste[k]:
                    taste[k] = True
    if False not in taste:
        ans = min(ans, i_bin.count('1'))

print(ans)
