h,m = map(int,input().split())
while True:
    mish = h//10*10+m//10
    mism = (h-h//10*10)*10+(m-m//10*10)
    #print(mish,mism)
    if mish<24 and mism<60:
        break
    else:
        m += 1
        if m == 60:
            m = 0
            h += 1
        if h == 24:
            h = 0
    #print(h,m)
print(h,m)