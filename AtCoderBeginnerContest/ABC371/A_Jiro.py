s_ab, s_ac, s_bc = input().split()

if s_ab != s_ac:
    print('A')
elif s_ab == s_bc:
    print('B')
else:
    print('C')
