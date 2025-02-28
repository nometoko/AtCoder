s = input()

mode = 0
const = 0
for i, c in enumerate(s):
    if c == 'W':
        mode = 1
        const += 1
    else:
        if c == 'A':
            if mode == 1:
                s = s[:i - const] + 'A' + 'C' * const + s[i + 1:]
        const = 0
        mode = 0
print(s)
