import math

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    pos = [0] * n
    prime = []
    for i in range(0, n):
        if isPrime(a[i]):
            pos[i] = 1
            prime.append(a[i])
    
    idx = 0
    prime.sort()
    for i in range(0, n):
        if pos[i] == 1:
            print(prime[idx], end = ' ')
            idx += 1
        else:
            print(a[i], end = ' ')
