import math

p = [True] * 1000005

def sieve():
    p[0] = p[1] = False
    for i in range(2, math.isqrt(1000005) + 1):
        if p[i]:
            for j in range(i * i, 1000005, i):
                p[j] = False

if __name__ == '__main__':
    sieve()
    for _ in range(0, int(input())):
        n = int(input())
        res = 0
        for i in range(2, n + 1):
            if i + 6 <= n and p[i] and p[i + 2] and p[i + 6]:
                res += 1
            elif i + 6 <= n and p[i] and p[i + 4] and p[i + 6]:
                res += 1
        print(res)