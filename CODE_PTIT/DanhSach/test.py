import math

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
    f = [0] * (m + 1)
    f[1] = b[0]
    for i in range(1, m):
        f[i + 1] = f[i] + b[i]
    
    print(b)
    print(f)
    





