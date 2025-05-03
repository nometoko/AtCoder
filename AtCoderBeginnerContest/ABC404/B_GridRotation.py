n = int(input())

s = [list(input()) for _ in range(n)]
t = [list(input()) for _ in range(n)]

def rotate(s):
  rotated = [[''] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      rotated[j][n - 1 - i] = s[i][j]
  return rotated

ans = float('Infinity')
for rotate_cnt in range(4):

  cnt = 0
  for i in range(n):
    for j in range(n):
      if s[i][j] != t[i][j]:
        cnt += 1
  ans = min(ans, cnt + rotate_cnt)
  s = rotate(s)

print(ans)
