n = int(input())

comb = []
total_len = 0
for _ in range(n):
    c, l = input().split()
    l = int(l)
    total_len += l
    comb.append((c, l))

if total_len > 100:
    print("Too Long")
else:
    for c, l in comb:
        print(c * l, end="")
    print()
