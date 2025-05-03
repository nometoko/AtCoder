n, m = map(int, input().split())

def base3(num):
  if num == 0:
    return [0]
  ans = []
  while num > 0:
    ans.append(num % 3)
    num //= 3
  return ans[::-1]

c = list(map(int, input().split()))

animal_dict = dict()

for i in range(m):
  zoos = list(map(int, input().split()))
  for zoo in zoos[1:]:
    if zoo not in animal_dict:
      animal_dict[zoo] = set()
    animal_dict[zoo].add(i + 1)

# bit探索の3進数ver
ans = float('Infinity')
for i in range(0, 3 ** n):
  # 3進数に変換
  bits = base3(i)
  # 3進数の桁数をnに合わせる
  while len(bits) < n:
    bits.insert(0, 0)

  animal_cnt = [0] * m
  for zoo, bit in enumerate(bits):
    for animal in animal_dict[zoo + 1]:
      animal_cnt[animal - 1] += bit

  ISBREAK = False
  for i in range(m):
    if animal_cnt[i] < 2:
      # print(bits, animal_cnt)
      ISBREAK = True
      break

  if not ISBREAK:
    money = sum([c * num for c, num in zip(c, bits)])
    # print(bits, money, animal_cnt)
    ans = min(ans, money)

print(ans)
