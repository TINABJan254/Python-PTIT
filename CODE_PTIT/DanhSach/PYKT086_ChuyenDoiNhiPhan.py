with open('DATA.in', 'r') as fo:
    for _ in range(int(fo.readline().strip())):
        b = int(fo.readline().strip())
        n = fo.readline().strip()
        n_10 = int(n, 2)
        if b == 2:
            print(n)
        elif b == 8:
            print(str(oct(n_10))[2:])
        elif b == 16:
            print(str(hex(n_10))[2:].upper())
        elif b == 4:
            res = ''
            while n_10 != 0:
                res += str(n_10 % 4)
                n_10 //= 4
            res = res[::-1]
            print(res)
