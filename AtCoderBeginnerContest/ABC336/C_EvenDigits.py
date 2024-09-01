n = int(input()) - 1
if n == 0:
    print(0)
    exit()
ans = []
while n >= 1:
    amari = n % 5
    ans.append(amari * 2)
    n //= 5

print(*ans[::-1], sep='')
