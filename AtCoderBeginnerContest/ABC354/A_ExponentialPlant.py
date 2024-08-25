h = int(input())

i = 1
height = 1
while height <= h:
    height += 2 ** i
    i += 1

print(i)
