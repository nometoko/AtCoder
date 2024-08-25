s = input()

mode = 0
for i in range(len(s)):
    if mode == 0:
        if s[i] == "A":
            continue
        elif s[i] == "B":
            mode = 1
        else:
            mode = 2
    elif mode == 1:
        if s[i] == "A":
            print("No")
            exit()
        elif s[i] == "B":
            continue
        else:
            mode = 2
    else:
        if s[i] == "A":
            print("No")
            exit()
        elif s[i] == "B":
            print("No")
            exit()
        else:
            continue

print("Yes")
