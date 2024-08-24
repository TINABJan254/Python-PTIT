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
        #hai số x1, x2 có thể nằm trên cùng 1 dòng, hoặc trên 2 dòng
        a = list(map(int, input().split()))
        if (len(a) == 1):
            x1 = a[0]
            x2 = int(input())
        else:
            x1, x2 = a[0], a[1]
        
        if p < q: p, q = q, p
        sum_max = gen(gen(x1, p, q), -1, -1) + gen(gen(x2, p, q), -1, -1)
        sum_min = gen(gen(x1, q, p), -1, -1) + gen(gen(x2, q, p), -1, -1)

        print(sum_min, sum_max)


