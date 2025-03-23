from bisect import bisect_left, bisect_right

n = int(input())

x = list(map(int, input().split()))
p = list(map(int, input().split()))

p_sum_list = [0] * (n + 1)
p_sum_list[0] = 0
for i in range(n):
  p_sum_list[i + 1] = p_sum_list[i] + p[i]

# print(p_sum_list)

q = int(input())

for _ in range(q):
  a, b = map(int, input().split())
  left_idx = bisect_left(x, a)
  right_idx = bisect_right(x, b)
  # print(f"({left_idx}, {right_idx}), {p_sum_list[right_idx]} - {p_sum_list[left_idx]}")
  print(p_sum_list[right_idx] - p_sum_list[left_idx])
