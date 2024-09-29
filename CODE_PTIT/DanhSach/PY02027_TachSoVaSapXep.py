res = []
for _ in range(0, int(input())):
    s = input()
    tmp = ''
    for i in range(0, len(s)):
        if (s[i].isnumeric()):
            tmp += s[i]
        else:
            tmp += ' ';

    a = list(map(int, tmp.split()))
    for x in a:
        res.append(x)

res.sort()
for x in res:
    print(x)