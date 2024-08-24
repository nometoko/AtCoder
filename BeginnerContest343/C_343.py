def check(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


n = int(input())
ans = 1
tmp = 1
for i in range(2, int(n ** (1 / 3)) + 2):
    tmp = i ** 3
    if tmp <= n and check(str(tmp)):
        ans = tmp

print(ans)
