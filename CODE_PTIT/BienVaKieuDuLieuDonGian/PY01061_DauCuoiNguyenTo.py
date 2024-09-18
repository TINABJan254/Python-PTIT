import math

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1    

if __name__ == '__main__':
    for _ in range(0, int(input())):
        n = input()
        if isPrime(int(n[:3])) and isPrime(int(n[-3:])):
            print('YES')
        else:
            print('NO')


