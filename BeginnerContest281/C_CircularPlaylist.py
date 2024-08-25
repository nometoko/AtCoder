n,t = map(int,input().split())
a = list(map(int,input().split()))
judge = 0
    
sum_a = sum(a)
t = t%sum_a
for i in range(n):
    pre_t = t
    t -= a[i]
    if t <= 0:
        print(i+1,pre_t)
        judge = 1
        break