s = input()
res = set()
for i in range(0, len(s), 2):
    k = int(s[i])
    if (i + 1 < len(s)):
        k = k * 10 + int(s[i + 1])
        res.add(k)
for x in sorted(res):
    print(x, end = " ")
