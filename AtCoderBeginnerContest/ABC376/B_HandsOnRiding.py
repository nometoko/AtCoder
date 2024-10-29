n, q = map(int, input().split())

count = 0
r = 2
l = 1

for _ in range(q):
    lr, num = input().split()
    num = int(num)
    if lr == 'R':
        if num < r:
            if num < l < r:
                count += (n - r) + num
            else:
                count += (r - num)
        else:
            if r < l < num:
                count += (n - num) + r
            else:
                count += (num - r)
        r = num
    if lr == 'L':
        if num < l:
            if num < r < l:
                count += (n - l) + num
            else:
                count += (l - num)
        else:
            if l < r < num:
                count += (n - num) + l
            else:
                count += (num - l)
        l = num
print(count)
