from functools import cmp_to_key

def cmp(x, y):
    if x < 0 and y >= 0:
        return -1
    if x >= 0 and y < 0:
        return 1
    return 0

if __name__ == '__main__':
    for _ in range(0, int(input())):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        maxE = max(a)
        for i in range(0, n):
            if a[i] == maxE:
                a = a[:i:] + [m] + a[i::]
                break
        
        a.sort(key = cmp_to_key(cmp))
        print(*a)