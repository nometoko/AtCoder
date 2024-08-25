x,k = map(int,input().split())

def rounding(a,b):
    i = a/10**(b)
    if i-int(i)>=0.5:
        i = int(i+1)*10**(b)
    else:
        i = int(i)*10**(b)
    return i

for i in range(1,k+1):
    x = rounding(x,i)
print(x)