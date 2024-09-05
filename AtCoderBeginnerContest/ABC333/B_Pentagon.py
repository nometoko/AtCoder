s = input()
t = input()

pentagon = 'ABCDE'
s_dist = abs(pentagon.index(s[0]) - pentagon.index(s[1]))
t_dist = abs(pentagon.index(t[0]) - pentagon.index(t[1]))
if min(s_dist, 5 - s_dist) == min(t_dist, 5 - t_dist):
    print('Yes')
else:
    print('No')
