import math 

if __name__ == '__main__':
    a, k, n = map(int, input().split())
    check = False
    b = k - (a % k)
    found = False
    while a + b <= n:
        print(b, end = ' ')
        found = True
        b += k
    if not found: print("-1")
