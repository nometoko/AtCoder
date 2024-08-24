s = input()
setS = set(s)
for char in set(s):
    if s.count(char) == 1:
        print(s.find(char) + 1)
