n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

for i in range(n - 1):
    if(a[i] == a[i+1]):
        print('stay')
        continue

    if(a[i] > a[i+1]):
        print('down ' + str(abs(a[i] - a[i+1])))

    if(a[i] < a[i+1]):
        print('up ' + str(abs(a[i] - a[i+1])))
