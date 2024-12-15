from collections import deque

abcde = list(map(int, input().split()))

scores = []
nameList = ['A', 'B', 'C', 'D', 'E']
for i in range(1, 32):
    binary = bin(i)[2:]
    # reverse
    binary = binary[::-1]
    score = 0
    name = []
    for i, bitI in enumerate(binary):
        if bitI == '1':
            score += abcde[i]
            name.append(nameList[i])
    scores.append([score, name])
        
scores.sort(reverse=True)

i = 0
stack = deque()
while i < 31:
    if i < 30 and scores[i][0] != scores[i + 1][0]:
        print(*scores[i][1], sep='')
        if len(stack) > 0:
            while len(stack) > 0:
                print(*stack.pop(), sep='')

    else:
        stack.append(scores[i][1])
    i += 1

if len(stack) > 0:
    while len(stack) > 0:
        print(*stack.pop(), sep='')
