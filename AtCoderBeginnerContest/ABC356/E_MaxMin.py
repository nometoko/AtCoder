import bisect

n = int(input())

a = list(map(int, input().split()))
a.sort()

a_max = a[-1]
cnt = [0] * (a_max + 1)
cnt_sum = [0] * (a_max + 1)

for num in a:
    cnt[num] += 1

for num in range(1, a_max + 1):
    cnt_sum[num] = cnt_sum[num - 1] + cnt[num]

ans = 0
# print(cnt_sum)
# print(a)
for num in set(a):
    # print(f"base {num}")
    max_mul = a_max // num

    ans += cnt[num] * (cnt[num] - 1) // 2
    # print(f"self cnt {cnt[num]}: {cnt[num] * (cnt[num] - 1) // 2}")

    for mul in range(1, max_mul + 1):
        mul_cnt = cnt_sum[min(num * (mul + 1) - 1, a_max)] - cnt_sum[num * mul - 1]

        if mul == 1:
            mul_cnt -= cnt[num]
        # print(f"comparing {num * (mul + 1) - 1} with {num * mul - 1} is {mul_cnt}")

        mul_cnt *= mul * cnt[num]
        ans += mul_cnt
        # print(f"\t{num} * {mul}: {mul_cnt}")
print(ans)
