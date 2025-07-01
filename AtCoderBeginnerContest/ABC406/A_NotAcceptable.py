a, b, c, d = map(int, input().split())

if a < c:
    print("No")
elif a > c:
    print("Yes")
else:
    if b < d:
        print("No")
    elif b > d:
        print("Yes")
