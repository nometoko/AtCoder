ABCDEF = list(map(int,input().split()))
ans = (ABCDEF[0]*ABCDEF[1]*ABCDEF[2]-ABCDEF[3]*ABCDEF[4]*ABCDEF[5])% 998244353
print(ans)