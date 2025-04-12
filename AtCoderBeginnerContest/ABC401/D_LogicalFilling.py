n, k = map(int, input().split())
s = input()

o_cnt = s.count('o')
p_cnt = s.count('.')

k -= o_cnt


if k == 0:
  print(s.replace('?', '.'))
  exit()

s = list(s)

if s[0] == 'o':
  s[1] = '.'

if s[-1] == 'o':
  s[-2] = '.'

for i in range(1, len(s) - 1):
  if s[i] == 'o':
    s[i - 1] = '.'
    s[i + 1] = '.'

q_cnt = s.count('?')

if q_cnt == 0:
  print(''.join(s))
  exit()

odd_cnt = 0

mode = 0
cnt = 0
max_o = 0
odd_ind = []

for i in range(len(s)):
  if s[i] == '?':
    mode = 1
    cnt += 1
  else:
    if mode == 1:
      if cnt % 2 == 1:
        odd_cnt += 1
        max_o += cnt // 2 + 1
        odd_ind.append(((i - cnt), cnt))
      else:
        max_o += cnt // 2

      cnt = 0
      mode = 0

if mode == 1:
  if cnt % 2 == 1:
    odd_cnt += 1
    max_o += cnt // 2 + 1
    odd_ind.append(((len(s) - cnt), cnt))
  else:
    max_o += cnt // 2


if (odd_cnt == 0) or (odd_cnt > 0 and max_o != k):
  print(''.join(s))
  exit()

for ind, length in odd_ind:
  for_o = True
  for i in range(length):
    if for_o:
      s[ind + i] = 'o'
    else:
      s[ind + i] = '.'
    for_o = not for_o

print(''.join(s))
