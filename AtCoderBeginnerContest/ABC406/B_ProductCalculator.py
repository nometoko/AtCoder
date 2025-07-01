n, k = map(int, input().split())

a = list(map(int, input().split()))

showing = 1
for num in a:
    showing *= num
    if showing >= 10**k:
        showing = 1

print(showing)
