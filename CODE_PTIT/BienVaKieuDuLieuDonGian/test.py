import math

prime = [True] * 8000
p = []

m = [3, 5, 5]

def sieve():
    prime[0] = prime[1] = False
    for i in range(2, math.isqrt(8000) + 1):
        if prime[i]:
            for j in range(i * i, 8000, i):
                prime[j] = False

    p.append(2)
    for i in range(3, 8000):
        if prime[i]:
            p.append(i)

if __name__ == '__main__':
    for i in range(0, 10):
        print(m[i])