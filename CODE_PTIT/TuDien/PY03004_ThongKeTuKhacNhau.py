from functools import cmp_to_key


def cmp(a, b):
    if a[1] != b[1]:
        return b[1] - a[1]
    if a[0] < b[0]: return -1
    return 1

n = int(input())
m = {}
for _ in range(n):
    s = ''
    for c in input().lower() + ' ':
        if c.isalpha() or c.isdigit(): 
            s += c
        else:
            if s != '':
                if s in m: m[s] += 1
                else: m[s] = 1
                s = ''

a = list(m.items())
a.sort(key = cmp_to_key(cmp))

for x in a:
    print(x[0], x[1])


'''
3
PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.
'''
