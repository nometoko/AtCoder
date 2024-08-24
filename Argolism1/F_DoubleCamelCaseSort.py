s = input()
words = []
start = 0
end = 0
state = 0
for i in range(len(s)):
    if s[i].isupper():
        if state == 0:
            start = i
            state = 1
        else:
            end = i
            words.append(s[start:end + 1])
            state = 0

words.sort(key = str.lower)
print(''.join(words))