n, c1, c2 = input().split()
n = int(n)
s = input()

for c in s:
    if c == c1:
        print(c1, end='')
    else:
        print(c2, end='')
print()
