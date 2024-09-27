import math

n = int(input())
a = []

for i in range(0, n):
    tmp = list(map(int, input().split()))
    a.append(tmp)
k = int(input())

s1, s2 = 0, 0
for i in range(0, n):
    for j in range(0, n - i - 1):
        s1 += a[i][j]

for i in range(0, n):
    for j in range(n - i, n):
        s2 += a[i][j]


print('YES') if abs(s1 - s2) <= k else print('NO')
print(abs(s1 - s2))