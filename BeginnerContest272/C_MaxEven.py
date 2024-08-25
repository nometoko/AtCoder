n = int(input())
a = list(map(int,input().split()))
guusuu = []
kisuu = []
if len(a)==2 and a[0]%2+a[1]%2==1:
    print(-1)
else:
    a.sort(reverse=True)
    cnt = 0
    for j in a:
        if(j%2 == 0):
            guusuu.append(j)
            if len(guusuu) == 2:
                break
    for j in a:
        if(j%2 == 1):
            kisuu.append(j)
            if len(kisuu) == 2:
                break
    if len(guusuu)<2:
        print(kisuu[0]+kisuu[1])
    elif len(kisuu)<2:
        print(guusuu[0]+guusuu[1])
    else:
        print(max(guusuu[0]+guusuu[1],kisuu[0]+kisuu[1]))