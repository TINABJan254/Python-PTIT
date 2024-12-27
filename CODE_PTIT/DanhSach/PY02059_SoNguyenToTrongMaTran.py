import math

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(0, n):
        a.append(list(map(int, input().split())))
    
    res = -1
    for x in a:
        for y in x:
            if isPrime(y) and y > res: res = y
    
    if res == -1:
        print('NOT FOUND')
    else: 
        print(res)
        for i in range(0, n):
            for j in range(0, m):
                if a[i][j] == res:
                    print(f'Vi tri [{i}][{j}]')
