s = 'wbwbwwbwbwbw'
w, b = map(int, input().split())
sLen = len(s)
s = s * (((w + b) // sLen) + 2)
sLen = len(s)
i = 0
# print(s)
while i + w + b < sLen:
    tmp = s[i:i + w + b]
    # print(len(tmp))
    if tmp.count('w') == w and tmp.count('b') == b:
        print('Yes')
        exit(0)
    i += 1

print('No')
