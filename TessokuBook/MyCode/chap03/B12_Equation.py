def calc(x):
    return x**3 + x


n = int(input())
maximum = n
minimum = 0
x = n / 2
num = calc(x)
while abs(num - n) > 0.001:
    # print(num, maximum, minimum)
    if num > n:
        maximum = x
        x = (minimum + x) / 2
    else:
        minimum = x
        x = (maximum + x) / 2
    num = calc(x)
print(x)
