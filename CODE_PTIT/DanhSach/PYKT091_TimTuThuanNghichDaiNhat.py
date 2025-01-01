from functools import cmp_to_key

def isPalindrome(s):
    return s == s[::-1]

def cmp(a, b):
    return len(b) - len(a)

#main
with open('CODE_PTIT/DanhSach/VANBAN.in', 'r') as fo:
    contents = fo.read()

a = [word for word in contents.strip().split() if isPalindrome(word)]
d = {}
for x in a:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

a.sort(key = cmp_to_key(cmp))

for x in a:
    if len(x) == len(a[0]):
        if (d[x] != 0):
            print(f'{x} {d[x]}')
            d[x] = 0
    else:
        break