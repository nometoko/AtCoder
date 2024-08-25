a, b, c = map(int, input().split())

if b < c:
    if a < b or c <= a:
        print('Yes')
    else:
        print('No')
else:
    if c <= a < b:
        print('Yes')
    else:
        print('No')
