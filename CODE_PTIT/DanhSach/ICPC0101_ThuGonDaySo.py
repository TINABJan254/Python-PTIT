import math

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    check = True
    while check:
        i = 0
        check = False
        while i < len(a) - 1:
            if (a[i] + a[i + 1]) % 2 == 0:
                check = True
                a[i:i+2] = []
                continue
            i += 1

    print(len(a))