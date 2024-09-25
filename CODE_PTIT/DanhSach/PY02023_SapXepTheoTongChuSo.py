from functools import cmp_to_key

def sumDigit(n):
    return sum(list(map(int, str(n))), 0)

def cmp(a, b):
    if sumDigit(a) != sumDigit(b):
        return sumDigit(a) - sumDigit(b)
    return a - b

if __name__ == '__main__':
    for _ in range(0, int(input())):
        n = int(input())
        a = list(map(int, input().split()))

        a.sort(key = cmp_to_key(cmp))
        for x in a:
            print(x, end = ' ')
        print()