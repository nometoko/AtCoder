import math
A,B = map(int,input().split())

def freefall(cor,i,sub):
    if (i-1)*B+A/math.sqrt(g+i-1) > cor:
        while True:
            i += sub
            pre = cor
            cor = i*B+A/math.sqrt(g+i)
            if cor - pre > 0:
                i -= sub
                return pre,i


    else:
        while True:
            if g+i <= sub:
                return cor,i
            else:
                i -= sub
                pre = cor
                cor = i*B+A/math.sqrt(g+i)
                if cor - pre > 0:
                    i += sub
                    return pre,i

pre = A
i = 1
g = 1
cor = i*B+A/math.sqrt(g+i)
if cor-pre > 0:
    print(pre)
else:
    sub = 1000000
    while True:
        if cor - pre > 0:
            cor = pre
            i -= sub
            break
        else:
            i += sub
            pre = cor
            cor = i*B+A/math.sqrt(g+i)


    while True:
        sub /= 10
        cor,i = freefall(cor,i,sub)
        if sub == 1:
            print(cor)
            break