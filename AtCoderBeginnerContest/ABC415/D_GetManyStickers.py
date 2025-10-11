n, m = map(int, input().split())

deals = []

for _ in range(m):
    a, b = map(int, input().split())
    deals.append((a - b, a, b))

deals.sort()
# print(deals)

ans = 0
for dec, a, b in deals:
    if n >= a:
        get_num = (n - a) // dec + 1
        ans += get_num
        n -= get_num * dec

    # print(f"dec = {dec}, a = {a}, b = {b}, n = {n}, ans = {ans}")

print(ans)
