def check(n):
    rev = 0
    cnt = 0
    tmp = n
    while n != 0:
        r = n % 10
        n //= 10
        if r != 2 and r != 0 and r != 4 and r != 6 and r != 8: return False
        cnt += 1
        rev = rev * 10 + r
    if cnt % 2 != 0 : return False
    return ((cnt > 1) and (rev == tmp))


if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        for i in range(1, n):
            if check(i) : print(i, end = ' ');
        print()