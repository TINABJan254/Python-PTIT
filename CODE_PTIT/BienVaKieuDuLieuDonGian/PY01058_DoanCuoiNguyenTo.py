import math

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

def check(n):
    tmp = int(n[len(n) - 4:])
    return isPrime(tmp)

if __name__ == '__main__':
    for _ in range(0, int(input())):
        n = input()
        if check(n):
            print('YES')
        else:
            print('NO')