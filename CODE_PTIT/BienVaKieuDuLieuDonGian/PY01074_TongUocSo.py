#TLE
import math

def ptich(n):
    res = 0
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            while (n % i == 0):
                res += i
                n //= i
    if n != 1:
        res += n
    return res


if __name__ == "__main__":
    res = 0
    for _ in range(0, int(input())):
        a = int(input())
        res += ptich(a)
    print(res)