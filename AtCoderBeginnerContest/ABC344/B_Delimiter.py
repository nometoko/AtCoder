a = list()
n = input()
while n != '0':
    a.append(n)
    n = input()
a.append(n)
a.reverse()
for i in a:
    print(i, end=' ')
