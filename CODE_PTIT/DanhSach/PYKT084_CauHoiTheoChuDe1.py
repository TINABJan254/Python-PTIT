a = []
for _ in range(0, int(input())):
    s = input()
    a.append(s)
    if s == "":
        print(a[0], len(a) - 2, sep = ": ")
        a.clear()
print(a[0], len(a) - 1, sep = ": ")