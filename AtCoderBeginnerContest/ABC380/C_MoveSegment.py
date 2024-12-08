n, k = map(int, input().split())
s = input()

state = int(s[0])
if state == 1:
    count = 1
else:
    count = 0

index = 0

while count != k - 1:
    if int(s[index]) != state:
        state = int(s[index])
        if state == 1:
            count += 1
    print(s[index], end='')
    index += 1

# k - 1 の1
while int(s[index]) == state:
    print(s[index], end='')
    index += 1

# k - 1, k の間の0
state = int(s[index])
zeroCount = 0
while int(s[index]) == state:
    index += 1
    zeroCount += 1

# k の1
state = int(s[index])
oneCount = 0
while index < n and int(s[index]) == state:
    index += 1
    oneCount += 1

for i in range(oneCount):
    print(1, end='')

for i in range(zeroCount):
    print(0, end='')

for i in range(index, len(s)):
    print(s[i], end='')
print()
