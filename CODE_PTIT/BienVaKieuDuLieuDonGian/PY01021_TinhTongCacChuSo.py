for _ in range(0, int(input())):
    s = input()
    t = 0
    res = ''
    for c in s:
        if c.isdigit():
            t += int(c)
        else:
            res += c
    res = ''.join(sorted(res))
    print(res + str(t))