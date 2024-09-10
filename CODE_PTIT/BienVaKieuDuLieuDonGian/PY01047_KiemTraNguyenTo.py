import math

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        s = input()
        n = int(s[len(s) - 4::])
        if isPrime(n):
            print('YES')
        else:
            print('NO')