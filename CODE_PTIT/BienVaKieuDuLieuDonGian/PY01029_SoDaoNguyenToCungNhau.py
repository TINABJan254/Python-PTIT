import math

t = int(input())
for _ in range(0, t):
    a = input()
    b = a[::-1]
    a = int(a)
    b = int(b)
    if math.gcd(a, b) == 1:
        print('YES')
    else:
        print('NO')