import math

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

def isPrimeDigit(n):
    for x in list(map(int, str(n))):
        if not isPrime(n):
            return False
    return True

if __name__ == '__main__':
    for _ in range(0, int(input())):
        n = int(input())
        if isPrimeDigit(n) and isPrime(n) and isPrime(int(str(n)[::-1])) and isPrime(sum(list(map(int, str(n))))):
            print('Yes')
        else:
            print('No')