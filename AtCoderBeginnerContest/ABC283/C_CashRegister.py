s = input()
i = 0
ans = len(s)
while i < len(s) - 1:
    if s[i] == s[i + 1] == '0':
        ans -= 1
        i += 1
    i += 1
print(ans)
