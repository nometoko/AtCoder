n, k = map(int, input().split())
s = input()

length = []
count = 0
for i in range(len(s)):
    if s[i] == 'O':
        count += 1
    else:
        if count != 0:
            length.append(count)
        count = 0

if count != 0:
    length.append(count)
ans = 0
for i in length:
    ans += i // k
print(ans)
