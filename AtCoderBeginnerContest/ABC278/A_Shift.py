n,k = map(int,input().split())
a = list(map(int,input().split()))
for i in range(k):
    a = a[1:]+[0]
print(*a)