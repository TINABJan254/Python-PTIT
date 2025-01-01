from functools import cmp_to_key

def cmp(a, b):
    if a[1] != b[1]: return b[1] - a[1]
    if a[0] < b[0]: return -1
    return 1

# main
n = int(input())
m = {}
for _ in range(n):
    s = ''
    for c in input().lower() + ' ':
        if c.isalpha():
            s += c
        else:
            if s != '':
                if s in m: m[s] += 1
                else: m[s] = 1
                s = ''

a = sorted(list(m.items()), key = cmp_to_key(cmp))
for x in a:
    print(x[0], x[1])
