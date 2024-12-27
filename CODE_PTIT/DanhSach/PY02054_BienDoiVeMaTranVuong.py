n, m = map(int, input().split())
a = []
for _ in range(0, n):
    a.append(list(map(int, input().split())))

if n > m:
    res = []
    cnt = n - m
    for i in range(0, n):
        if cnt != 0 and i % 2 == 0:
            cnt -= 1 
            continue
        res.append(a[i])
    a = res
elif n < m:
    res = []
    cnt = m - n
    t_a = [[row[i] for row in a] for i in range(len(a[0]))]
    for i in range(0, m):
        if cnt != 0 and i % 2 != 0:
            cnt -= 1
            continue
        res.append(t_a[i])
    a = [[row[i] for row in res] for i in range(len(res[0]))]

#result
for i in range(0, len(a)):
    for j in range(0, len(a[0])):
        print(a[i][j], end = ' ')
    print()