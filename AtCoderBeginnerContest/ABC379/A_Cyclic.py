n = int(input())

a = n // 100
b = n // 10 - a * 10
c = n % 10

print(str(b) + str(c) + str(a), str(c) + str(a) + str(b), sep=' ')
