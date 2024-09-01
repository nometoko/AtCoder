n = int(input())
s = list(input())

quote_num = 0
for i in range(n):
    if s[i] == '"':
        quote_num += 1
    elif s[i] == ',' and quote_num % 2 == 0:
        s[i] = '.'

print(*s, sep='')
