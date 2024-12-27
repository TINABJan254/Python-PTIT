import math

def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n = int(input())
    tmp = list(map(int, input().split()))
    d = {}
    for x in tmp:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    a = list(d.keys())
    found = False
    for i in range(0, len(a) - 1):
        if isPrime(sum(a[0:i+1], 0)) and isPrime(sum(a[i+1:], 0)):
            print(i)
            found = True
            break
    if not found:
        print("NOT FOUND")
