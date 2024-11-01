import math

def sumFac(n):
    res = 0
    for x in list(map(int, str(n))):
        res += math.factorial(x)
    return res

if __name__ == '__main__':
    for _ in range(0, int(input())):
        n = int(input())
        if n == sumFac(n):
            print('Yes')
        else:
            print('No')