s = list(input())
t = list(input())

ans = []
while s != t:
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[i] > t[i]:
                s[i] = t[i]
                ans.append(s.copy())
    for i in range(len(s) - 1, -1, -1):
        if s[i] != t[i]:
            if s[i] < t[i]:
                s[i] = t[i]
                ans.append(s.copy())

print(len(ans))
for a in ans:
    print("".join(a))
