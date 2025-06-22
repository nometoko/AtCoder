DEBUG = False

t = int(input())


for _ in range(t):
    length = int(input())
    s = list(input())

    if length == 1:
        print(s[0])
        continue

    rot_start = -1
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            rot_start = i
            break
        print(s[i], end="")

    if rot_start == -1:
        print(s[-1])
        continue

    rot_s_char = s[rot_start]
    rot_end = length

    if DEBUG:
        print(f"Found rotation start at index {rot_start} with character {rot_s_char}")

    for i in range(rot_start + 1, length + 1):
        if i == length or rot_s_char < s[i]:
            if DEBUG and i != length:
                print(f"Found rotation end at index {i} with character {s[i]}")
            rot_end = i
            print(rot_s_char, end="")
            break
        print(s[i], end="")

    if DEBUG and rot_end != length:
        print(f"Final rotation end at index {rot_end} with character {s[rot_end]}")

    for i in range(rot_end, length):
        print(s[i], end="")

    print()
