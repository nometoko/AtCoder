versions = ["Ocelot", "Serval", "Lynx"]

x, y = input().split()

if versions.index(x) >= versions.index(y):
    print("Yes")
else:
    print("No")
