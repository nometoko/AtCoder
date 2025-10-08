t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    count_0 = s.count("0")
    count_1 = s.count("1")

    max_continuous_length = [-1, -1]

    continuous_len = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            continuous_len += 1
        else:
            continuous_val = int(s[i - 1])
            if continuous_len > max_continuous_length[continuous_val]:
                max_continuous_length[continuous_val] = continuous_len

            continuous_len = 1

    if continuous_len > max_continuous_length[int(s[-1])]:
        max_continuous_length[int(s[-1])] = continuous_len

    # print(f"{max_continuous_value}, {max_continuous_length}")
    ans1 = (count_0 - max_continuous_length[0]) * 2 + count_1
    ans2 = (count_1 - max_continuous_length[1]) * 2 + count_0
    print(min(ans1, ans2))
