def check(s):
    if not s.isdigit(): return True
    tmp = int(s)
    if -2**31 <= tmp <= 2**31-1: return False
    return True

# main
res = []
with open('DATA.in', 'r') as fo:
    for line in fo:
        for x in line.strip().split():
            if check(x): res.append(x)

res.sort()
for x in res:
    print(x, end = ' ')
