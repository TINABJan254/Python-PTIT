import math
a, b, n = map(int, input().split())
check = False
for x in range(0, n // a + 1):
    tmp = n - a * x
    if tmp % b == 0:
        check = True
        print(x, tmp // b)
if not check:
    print("NO")