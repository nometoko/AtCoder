n = input()
ans = 0
for i in reversed(range(len(n))):
    if int(n[i]) == 1:
        ans += 2 ** (len(n) - 1 - i)
print(ans)
