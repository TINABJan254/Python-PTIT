from functools import cmp_to_key
import sys

def cmp(x, y):
    if x % 2 == 0 and y % 2 == 0: return x - y
    if x % 2 != 0 and y % 2 != 0: return y - x
    return 0

if __name__ == '__main__':
    n = int(input())
    a = []
    while len(a) < n:
        a += list(map(int, input().split()))
    a.sort(key = cmp_to_key(cmp))
    print(*a)

