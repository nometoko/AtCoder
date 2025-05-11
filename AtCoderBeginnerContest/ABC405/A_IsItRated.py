r, x = map(int, input().split())

if x == 1:
    if 1600 <= r < 3000:
        print("Yes")
    else:
        print("No")

else:
    if 1200 <= r < 2400:
        print("Yes")
    else:
        print("No")
