s = input()
index = [0] * 2
index[0] = s.find('|')
index[1] = s.rfind('|')
print(s[:index[0]] + s[index[1] + 1:])
