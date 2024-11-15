import math
import sys

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    d = dict()
    for x in a:
        if x not in d:
            b.append(x)
            d[x] = 1
    m = len(b)
    f = [0] * m
    f[0] = b[0]
    for i in range(1, m):
        f[i] = f[i - 1] + b[i]
    
    for i in range(0, m):
        if isPrime(f[i]) and isPrime(f[m - 1] - f[i]):
            print(i)
            sys.exit()
    
    print('NOT FOUND')
