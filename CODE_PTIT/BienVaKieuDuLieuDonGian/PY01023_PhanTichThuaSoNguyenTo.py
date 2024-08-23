import math

def ptich(n):
    print("1 * ", end = '')
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            print(i, '^', cnt, sep = '', end = ' ')
            if n > 1: print('*', end = ' ')
    
    if n > 1: print(n, '^1', sep = '')
    else:
        print()


if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        ptich(n)