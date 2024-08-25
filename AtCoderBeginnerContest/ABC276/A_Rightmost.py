s = input()
cnt = 0
for i in reversed(range(0,len(s))):
    if s[i] == "a":
        print(i+1)
        cnt = 1
        break
if cnt == 0:
    print(-1)