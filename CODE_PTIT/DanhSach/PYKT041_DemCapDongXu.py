n = int(input())
a = []
for i in range(0, n):
    a.append(input())

res = 0
for i in range(0, n):
    cnt = 0
    for j in range(0, n):
        if a[i][j] == 'C': cnt += 1
    res += (cnt * (cnt - 1)) // 2

for i in range(0, n):
    cnt = 0
    for j in range(0, n):
        if a[j][i] == 'C': cnt += 1
    res += (cnt * (cnt - 1)) // 2

print(res)