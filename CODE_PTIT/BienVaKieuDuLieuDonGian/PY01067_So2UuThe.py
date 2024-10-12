from functools import cmp_to_key

f = []

def check(n):
    if n[0] == '0': return False
    if n.count('2') > len(n) // 2:
        return True
    return False

def Try(s):
    for i in range(0, 3):
        new_s = s + str(i)
        if check(new_s):
            f.append(new_s)
        if len(new_s) < 10:
            Try(new_s)

def cmp(x, y):
    if len(x) != len(y):
        return len(x) - len(y)
    if x < y:
        return -1
    return 1    

if __name__ == '__main__':
    Try('')
    f.sort(key = cmp_to_key(cmp))

    for _ in range(0, int(input())):
        n = int(input())
        for i in range(0, n):
            print(f[i], end = ' ')
        print()