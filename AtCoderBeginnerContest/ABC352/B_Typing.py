s = input()
t = input()

ans = 0
for char in s:
    tmp = t[ans:].find(char)
    ans += tmp + 1
    print(ans, end=' ')
