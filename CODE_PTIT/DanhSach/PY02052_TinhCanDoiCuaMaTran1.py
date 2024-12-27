n = int(input())
a = []
for _ in range(0, n):
    a.append(list(map(int, input().split())))
k = int(input())

sum1 = 0 # nua tren
sum2 = 0 # nua duoi

for i in range(0, n):
    for j in range(i + 1, n):
        sum1 += a[i][j]
        sum2 += a[j][i]

if abs(sum1 - sum2) <= k:
    print('YES')
else:
    print('NO')
print(abs(sum1 - sum2))


