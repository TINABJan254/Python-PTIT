from functools import cmp_to_key
import sys

def cmp(x, y):
    if x % 2 == 0 and y % 2 == 0: return x - y
    if x % 2 != 0 and y % 2 != 0: return y - x
    return 0

if __name__ == '__main__':
    n = int(input())
    a = []
    while len(a) < n:
        a += list(map(int, input().split()))
    
    pos = [0] * n
    even, odd = [], []
    for i in range(0, n):
        if a[i] % 2 == 0:
            even.append(a[i])
        else:
            pos[i] = 1
            odd.append(a[i])
    even.sort()
    odd.sort(reverse = True)

    i, j = 0, 0
    for k in range(0, n):
        if pos[k] == 1:
            print(odd[i], end = ' ')
            i += 1
        else:
            print(even[j], end = ' ')
            j += 1


    

