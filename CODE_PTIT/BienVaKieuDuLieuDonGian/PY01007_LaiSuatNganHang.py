import math
t = int(input())
for _ in range(0, t):
    n, x, m = map(float, input().split())
    print(math.ceil(math.log(m / n) / math.log(1 + x/100)))