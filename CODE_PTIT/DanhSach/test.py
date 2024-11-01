p = [True] * 10000005;

def sieve():
    p[0] = p[1] = False
    for i in range(2, 1000):
        if p[i]:
            for j in range(i * i, 10000005, i):
                p[j] = False

def check(n):
    if not p[n] or not p[int(str(n)[::-1])]: return False
    if not p[sum(list(map(int, str(n))))]: return False
    for x in list(map(int, str(n))):
        if not p[x]: return False
    return True

if __name__ == '__main__':
    sieve()
    for _ in range(0, int(input())):
        n = int(input())