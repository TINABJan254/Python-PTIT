from functools import cmp_to_key

def mulDigit(n):
    res = 1
    for c in str(n):
        res *= int(c)
    
    return res

def cmp(a, b):
    if mulDigit(a) != mulDigit(b):
        return mulDigit(a) - mulDigit(b)
    return a - b

if __name__ == '__main__':
    for _ in range(0, int(input())):
        n = int(input())
        a = list(map(int, input().split()))

        a.sort(key = cmp_to_key(cmp))
        for x in a:
            print(x, end = ' ')
        print()