f = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if __name__ == "__main__":
    for _ in range(0, int(input())):
        n, base = map(int, input().split())
        ans = ''
        while n > 0:
            ans += f[n % base]
            n //= base
        print(ans[::-1])