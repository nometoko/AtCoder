n = int(input())
s = input()

if n % 2 != 1:
    print("No")
    exit()

if n == 1 and s == "/":
    print("Yes")
    exit()

tmp = list(set(s[: n // 2]))
# print(tmp)
if len(tmp) != 1 or tmp[0] != "1":
    print("No")
    exit()

if s[len(s) // 2] != "/":
    print("No")
    exit()

tmp = list(set(s[len(s) // 2 + 1 :]))
if len(tmp) != 1 or tmp[0] != "2":
    print("No")
    exit()

print("Yes")
