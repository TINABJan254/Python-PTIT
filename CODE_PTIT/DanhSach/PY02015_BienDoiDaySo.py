import math

if __name__ == '__main__':
    while True:
        a = list(map(int, input().split()))
        if sum(a) == 0: break

        res = 0
        while len(set(a)) != 1:
            res += 1
            tmp = a[0]
            for i in range(0, 3):
                a[i] = math.fabs(a[i] - a[i + 1])
            a[3] = math.fabs(a[3] - tmp)

        print(res)