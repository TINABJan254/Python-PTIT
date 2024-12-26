s = input()
res = {}
for i in range(0, len(s), 2):
    k = int(s[i])
    if (i + 1 < len(s)):
        k = k * 10 + int(s[i + 1])
        if k in res:
            res[k] += 1
        else:
            res[k] = 1

for x in res:
    print(x, res[x])