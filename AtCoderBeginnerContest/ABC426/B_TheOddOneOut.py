s = input()

chars = set(s)

for char in chars:
    if s.count(char) == 1:
        print(char)
