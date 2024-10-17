import math

p = [True] * 10005;
prime = []

def init():
    p[0] = p[1] = False
    for i in range(2, math.isqrt(10005) + 1):
        if p[i]:
            for j in range(i * i, 10005, i):
                p[j] = False

    for i in range(2, 10005):
        if p[i]: 
            prime.append(i)

if __name__ == '__main__':
    init()
    print(prime)
    # n = int(input())
    # a = list(map(int, input().split()))

    # res = 0
    # for i in range(0, n):
    #     tmp = 10**9
    #     for j in prime:
    #         tmp = min(tmp, j - a[i])
    #     res = max(tmp, res)
    
    # print(res)
