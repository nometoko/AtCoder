n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
card = []

ind = 0
for i in sorted(set(a)):
    card.append([i, 0])
    while ind < n and a[ind] == i:
        card[-1][1] += i
        ind += 1

sum_a = sum(a)
len_card = len(card)
s = [sum_a] * len_card
now = -1
for i in range(len_card):
    if i <= now:
        continue
    now = i
    s[i] -= card[i][1]
    diff = abs(card[(now + 1) % len_card][0] - card[now][0])
    while diff == 1 or diff == m - 1:
        now = (now + 1) % len_card
        s[i] -= card[now % len_card][1]
        if now == (i - 1) % len_card:
            break
        if card[now][0] == m - 1:
            s[i] -= sum_a - s[0]
            break
        diff = abs(card[(now + 1) % len_card][0] - card[now][0])

# print(s)
print(min(s))
