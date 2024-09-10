import math

def dao(n):
    res = 0
    while n != 0:
        res = res * 10 + n % 10
        n //= 10
    return res

if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        for _ in range(0, 1000):
            if n % 7 == 0:
                break
            n += dao(n)
        print(n)