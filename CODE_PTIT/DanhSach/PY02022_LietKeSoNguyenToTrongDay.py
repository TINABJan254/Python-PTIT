import math

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    d = {}
    for i in range(0, len(a)):
        if isPrime(a[i]):
            if a[i] in d:
                d[a[i]] += 1
            else:
                d[a[i]] = 1
    
    for i in range(0, len(a)):
        if a[i] in d:
            print(a[i], d[a[i]])
            d.pop(a[i])
