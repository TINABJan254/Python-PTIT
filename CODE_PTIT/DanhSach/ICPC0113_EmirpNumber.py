p = [True] * 1000005;

def sieve():
    p[0] = p[1] = False
    for i in range(2, 1000):
        if p[i]:
            for j in range(i * i, 1000005, i):
                p[j] = False

if __name__ == '__main__':
    sieve()
    for _ in range(0, int(input())):
        n = int(input())
        d = [True] * (n + 1)
        for i in range(10, n):
            if d[i] and p[i] and p[int(str(i)[::-1])] and i != int(str(i)[::-1]) and int(str(i)[::-1]) <= n:
                d[int(str(i)[::-1])] = False
                d[i] = False
                print(i, str(i)[::-1], sep = ' ', end = ' ')
        print()