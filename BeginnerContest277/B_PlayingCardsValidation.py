n = int(input())
s = []
cnt = []
for i in range(n):
    s.append(input())

for i in range(n):
    if (s[i][0]=="H" or s[i][0]=="D" or s[i][0]=="C" or s[i][0]=="S") and (s[i][1]=="A" or s[i][1]=="2" or s[i][1]=="3" or s[i][1]=="4" or s[i][1]=="5" or s[i][1]=="6" or s[i][1]=="7" or s[i][1]=="8" or s[i][1]=="9" or s[i][1]=="T" or s[i][1]=="J" or s[i][1]=="Q" or s[i][1]=="K"):
        cnt.append(1)
    else:
        cnt.append(0)
if 0 not in cnt and (len(s) == len(list(set(s)))):
    print("Yes")
else:
    print("No")