import math
import sys

s = set([])
for x in sys.stdin:
    a = list(map(int, x.split()))
    a = [a[i] % 42 for i in range(0, len(a))]
    s = s.union(a)

print(len(s))