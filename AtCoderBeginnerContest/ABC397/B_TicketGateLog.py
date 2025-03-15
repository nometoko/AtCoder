s = input()

count = 0
index = 0
lenS = len(s)
newIndex = 1

while index < lenS:
  if newIndex % 2 == 0:
    if s[index] == 'i':
      count += 1
    else:
      index += 1
  else:
    if s[index] == 'i':
      index += 1
    else:
      count += 1
  newIndex += 1

if newIndex % 2 == 0:
  count += 1
print(count)
