s = input()

letters = list(set(s))
ans = 0
for i in letters:
    if s.count(i) >= 2:
        ans += 1
        break

for i in range(len(letters) - 1):
    for j in range(i + 1, len(letters)):
        ans += s.count(letters[i]) * s.count(letters[j])


print(ans)
