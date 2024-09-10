import math

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

t = int(input())
for _ in range(0, t):
    n = input()
    a = list(map(int, n))
    sumDigit = sum(a, 0) #sum(iterable, giaTriKhoiTao)

    if isPrime(sumDigit):
        print('YES')
    else:
        print('NO')