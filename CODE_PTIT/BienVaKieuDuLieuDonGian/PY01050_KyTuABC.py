from functools import cmp_to_key
list = []

def check(s):
    cnta = s.count('A')
    cntb = s.count('B')
    cntc = s.count('C')
    return cnta * cntb * cntc > 0 and cnta <= cntb and cntb <= cntc and len(s) >= 3

def Try(i, s, n):
    if check(s):
        list.append(s)
    if i < n:
        Try(i + 1, s + 'A', n)
        Try(i + 1, s + 'B', n)
        Try(i + 1, s + 'C', n)

def cmp(a, b):
    if len(a) != len(b):
        return len(a) - len(b)
    return a < b

if __name__ == '__main__':
    n = int(input())
    Try(0, '', n)
    list.sort(key = cmp_to_key(cmp))
    for x in list:
        print(x)