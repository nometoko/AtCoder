a, b = map(int, input().split())
ans = False
for i in range(a, b + 1):
    if 100 % i == 0:
        ans = True

if ans:
    print("Yes")
else:
    print("No")
