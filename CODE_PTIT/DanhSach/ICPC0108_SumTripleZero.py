if __name__ == '__main__':
    for _ in range(0, int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        res = 0
        for i in range(0, n - 2):
            x = a[i]
            L = i + 1
            R = n - 1
            while L < R:
                if x + a[L] + a[R] == 0:
                    res += 1
                    L += 1
                elif x + a[L] + a[R] < 0:
                    L += 1
                else:
                    R -= 1
        print(res)