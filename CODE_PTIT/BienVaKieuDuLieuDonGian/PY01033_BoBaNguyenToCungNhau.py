import math

L, R = map(int, input().split())

for i in range(L, R-1):
    for j in range(i + 1, R):
        if math.gcd(i, j) == 1:
            for k in range(j + 1, R + 1):
                if math.gcd(k, j) == 1 and math.gcd(k, i) == 1:
                    print('(', i, ', ', j, ', ', k, ')', sep = '')