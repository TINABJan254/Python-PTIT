import math

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

def check(n):
    for i in range(0, len(n), 2): 
        if int(n[i]) % 2 != 0: return False
    for i in range(1, len(n), 2):
        if int(n[i]) % 2 == 0: return False
    
    if isPrime(sum(list(map(int, n)))):
        return True
    return False

if __name__ == '__main__':
    for _ in range(0, int(input())):
        n = input()
        if check(n): 
            print('YES')
        else: 
            print('NO')