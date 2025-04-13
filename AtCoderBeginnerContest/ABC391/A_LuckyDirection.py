direction = input()

for c in direction:
    if c == "E":
        print("W", end="")
    elif c == "W":
        print("E", end="")
    elif c == "N":
        print("S", end="")
    elif c == "S":
        print("N", end="")
print()
