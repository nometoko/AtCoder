s = input()
t = input()

for i in range(1, len(s)):
    if s[i] == s[i].upper():
        if s[i - 1] not in t:
            print("No")
            exit()

print("Yes")
