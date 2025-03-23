s = input()

chars = set()
lenS = len(s)
if lenS % 2 != 0:
    print("No")
    exit()

for i in range(len(s) // 2):
    if s[i * 2] != s[i * 2 + 1]:
        print("No")
        exit()
    else:
        if s[i * 2] in chars:
            print("No")
            exit()
        chars.add(s[i * 2])

print("Yes")
