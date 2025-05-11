n, m = map(int, input().split())

a = list(map(int, input().split()))

num_cnt = dict()

for num in a:
    if num not in num_cnt:
        num_cnt[num] = 0
    num_cnt[num] += 1

for num in range(1, m + 1):
    if num not in num_cnt:
        print(0)
        exit()

for i, num in enumerate(reversed(a)):
    num_cnt[num] -= 1

    if num_cnt[num] == 0:
        print(i + 1)
        exit()
