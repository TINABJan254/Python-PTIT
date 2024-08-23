import math

def sumDigit(n):
    res = 0
    while n != 0:
        res += n % 10
        n //= 10
    return res

def check(n):
    o1 = n % 10
    n //= 10
    while n != 0:
        o2 = n % 10
        n //= 10
        if math.fabs(o1 - o2) != 2.0:
            return False
        o1 = o2
    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        if sumDigit(n) % 10 == 0 and check(n):
            print("YES")
        else:
            print("NO")