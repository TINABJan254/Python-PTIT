import math

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

def check(n):
    if not isPrime(len(n)): return False
    cnt = 0
    for i in range(0, len(n)):
        if isPrime(int(n[i])): cnt += 1
    return cnt > len(n) - cnt

if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        n = input()
        if check(n):
            print('YES')
        else:
            print('NO')