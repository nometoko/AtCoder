n = int(input())
beans = dict()

for i in range(n):
    a, c = map(int, input().split())
    if c in beans.keys():
        if beans[c] > a:
            beans[c] = a
    else:
        beans[c] = a

print(max(beans.values()))
