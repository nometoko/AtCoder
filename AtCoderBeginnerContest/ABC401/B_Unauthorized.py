n = int(input())

authorized = False
cnt = 0
for _ in range(n):
  s = input()
  if s == 'login':
    authorized = True
  elif s == 'logout':
    authorized = False
  elif s == 'public':
    continue
  elif s == 'private':
    if not authorized:
      cnt += 1

print(cnt)
