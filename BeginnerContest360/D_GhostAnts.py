import bisect
n, t = map(int, input().split())
s = input()
x = list(map(int, input().split()))

right = [x[i] for i in range(n) if s[i] == '1']
left = [x[i] for i in range(n) if s[i] == '0']

left.sort()
right.sort()

# print(left)
# print(right)

ans = 0
for ant in right:
    # print(ant, bisect.bisect_right(left, ant + 2 * t), bisect.bisect_left(left, ant))
    ans += bisect.bisect_right(left, ant + 2 * t) - bisect.bisect_left(left, ant)
    # print(ans)
print(ans)
