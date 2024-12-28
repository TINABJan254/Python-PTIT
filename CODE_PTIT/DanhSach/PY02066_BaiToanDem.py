import sys

n = int(input())
a = []
for s in sys.stdin:
    a += list(map(int, s.split()))

d = [0] * (max(a) + 1)
for x in a:
    d[x] += 1

excellent = True
for i in range(1, max(a) + 1):
    if d[i] == 0:
        excellent = False
        print(i)

if excellent:
    print("Excellent!")