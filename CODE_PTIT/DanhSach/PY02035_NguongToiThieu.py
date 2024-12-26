s = input()
k = int(input())
res = {}
for i in range(0, len(s), 2):
    x = int(s[i])
    if (i + 1 < len(s)):
        x = x * 10 + int(s[i + 1])
        if x in res:
            res[x] += 1
        else:
            res[x] = 1

found = False
for x in sorted(res):
    if res[x] >= k:
        print(x, res[x])
        found = True

if (not found):
    print("NOT FOUND")