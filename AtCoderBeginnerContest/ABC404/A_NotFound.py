s = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in alphabet:
    if char not in s:
        print(char)
        break
