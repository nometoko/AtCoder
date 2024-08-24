n = int(input())

num1 = 3
num2 = 5
num3 = 7

num = n // num1 + n // num2 + n // num3
num -= n // (num1 * num2) + n // (num2 * num3) + n // (num3 * num1)
num += n // (num1 * num2 * num3)

print(num)
