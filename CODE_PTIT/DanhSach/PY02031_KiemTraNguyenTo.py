import math

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(0, n):
        a.append(list(map(int, input().split())))

    res = [[1 if isPrime(a[i][j]) else 0 for j in range(0, m)] for i in range(0, n)]
    
    for i in range(0, n):
        for j in range(0, m):
            print(res[i][j], end = ' ')
        print()