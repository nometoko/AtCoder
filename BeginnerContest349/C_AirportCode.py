s = input()
t = input()
index = 0

for i in range(len(t)):
    s = s[index:]
    index = s.find(t[i].lower())
    # print(index)
    # print(s)
    if i <= 1 and index == -1:
        print('No')
        exit(0)
    if i == 2 and index == -1 and t[i] != 'X':
        print('No')
        exit(0)
    index += 1
print('Yes')
