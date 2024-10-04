a = []
for _ in range(0, int(input())):
    a.append(len(input().split()))

res = []
i = 0
while i < len(a):
    if a[i] == 6:
        res.append(1)
        while (i < len(a) and a[i] == 6):
            i += 2
    else:
        res.append(2)
        i += 4
print(len(res))
for x in res:
    print(x)
