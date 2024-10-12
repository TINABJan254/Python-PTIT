import math

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(0, a[0])
    exit

min_step = 999999999
min_e = 9999999999
for i in range(0, n):
    cnt = 0
    for j in range(0, n):
        cnt += abs(a[i] - a[j])
    if cnt < min_step:
        min_step = cnt
        min_e = a[i]
print(min_step, min_e)
