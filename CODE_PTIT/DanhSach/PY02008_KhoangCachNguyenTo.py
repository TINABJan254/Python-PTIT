import math

prime = [True] * 8000
p = []

def sieve():
    prime[0] = prime[1] = False
    for i in range(2, math.isqrt(8000) + 1):
        if prime[i]:
            for j in range(i * i, 8000, i):
                prime[j] = False

    for i in range(2, 8000):
        if prime[i]:
            p.append(i)

if __name__ == '__main__':
    sieve()
    n, x = map(int, input().split())
    print(x, end = ' ')
    for i in range(0, n):
        x += p[i]
        print(x, end = ' ')