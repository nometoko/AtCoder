n = int(input())
h = list(map(int, input().split()))

t = 0
for enemy in h:
    while t % 3 != 0:
        if t % 3 == 1:
            if enemy > 0:
                enemy -= 1
                t += 1
            else:
                break
        if t % 3 == 2:
            if enemy > 0:
                enemy -= min(3, enemy)
                t += 1
            else:
                break
    
    if enemy > 0:
        plus = enemy // 5
        rest = enemy - plus * 5
        t += plus * 3
        if rest < 3:
            t += rest
        else:
            t += 3
print(t)
