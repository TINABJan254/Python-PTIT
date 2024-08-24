import math

def gen(n, p, q):
    res = 0
    while n != 0:
        c = n % 10
        if (c == q): c = p
        res = res * 10 + c
        n //= 10
    return res

if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        p, q = map(int, input().split())
        x1, x2 = map(int, input().split())
        
        if p < q: p = q
        print(p, q)
        # sum_max = gen(gen(x1, p, q), -1, -1) + gen(gen(x2, p, q), -1, -1)
        # sum_min = gen(gen(x1, q, p), -1, -1) + gen(gen(x2, q, p), -1, -1)

        # print(sum_min, sum_max)


