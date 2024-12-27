# a = [[0 for _ in range(n)] for _ in range(n)] : khai bao mang 2 chieu

n = int(input())
b = []
for _ in range(n):
    b.append(list(map(int, input().split())))

if n == 2:
    print(b[0][1] // 2)
else:
    tmp = [0] * n # tmp[i] = a[i] - a[i - 1]
    for i in range(1, n-1):
        tmp[i] = b[i][n-1] - b[i-1][n-1]
    tmp[n-1] = b[n-1][0] - b[n-2][0] # th rieng (vi b[n-1][n-1] = 0 => ko the dat trong vong for)

    a = []
    a.append(int((b[0][1] - tmp[1])/2))    
    for i in range(1, n):
        a.append(a[i - 1] + tmp[i])
    
    for x in a: print(x, end = ' ')

