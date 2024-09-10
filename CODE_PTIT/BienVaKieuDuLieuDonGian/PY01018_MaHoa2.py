import sys
if __name__ == '__main__':
    P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
    while True:
        tmp = input()
        if tmp == '0': sys.exit(0)
        a = list(tmp.split())
        k = int(a[0])
        s = a[1]
        res = ''
        for i in range(0, len(s)):
            res += P[(P.index(s[i]) + k) % 28]
        print(res[::-1])

