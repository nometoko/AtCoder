s = input()
set_s = sorted(list(set(s)))
max_char = set_s[0]
max_count = s.count(max_char)
for char in set_s:
    if s.count(char) > max_count:
        max_char = char
        max_count = s.count(char)
print(max_char)
