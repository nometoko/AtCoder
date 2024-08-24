n = int(input())
sweet = False
for i in range(n):
    s = input()
    if s == 'sweet':
        if sweet and i != n - 1:
            print('No')
            exit(0)
        else:
            sweet = True
    else:
        sweet = False

print('Yes')
