n = int(input())

ans = 0
for _ in range(n):
    ope, num = input().split()
    num = int(num)
    if ope == '+':
        ans += num
    elif ope == '-':
        ans -= num
    elif ope == '*':
        ans *= num
    ans = ans % 10000
    print(ans)
