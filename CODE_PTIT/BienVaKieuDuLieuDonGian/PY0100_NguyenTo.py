import math
t = int(input())
for i in range(0, t):
    n = int(input())
    k = 0
    for j in range(1, n):
        if math.gcd(n, j) == 1: k += 1
    check = True
    for j in range(2, math.isqrt(k) + 1):
        if k % j == 0: check = False
    if check and k > 1 : print("YES")
    else: print("NO")