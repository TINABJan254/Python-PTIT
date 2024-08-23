import math

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

def check(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return isPrime(sum)

if __name__ == '__main__':
    t = int(input())
    for _ in range(0,  t):
        a, b = map(int, input().split())
        if check(math.gcd(a, b)): print("YES")
        else: print("NO")