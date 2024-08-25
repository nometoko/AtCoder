import re
a = input()
if re.search(r'[A-Z]\d{6}[A-Z]',a):
    if len(a) == 8 and a[1] != '0':
        print('Yes')
    else:
        print("No")
else:
    print("No")