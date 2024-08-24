s = input()
if s[0] == '<' and s[-1] == '>' and s[1:-1].count('<') == 0 and s[1:-1].count('>') == 0:
    print('Yes')
else:
    print('No')
