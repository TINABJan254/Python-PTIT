dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    
    vs = [[False for i in range(0, m)] for j in range(0, n)]
    res = 0
    for i in range(0, n):
        for j in range(0, m):
            if a[i][j] == -1:
                for k in range(0, 8):
                    x1 = i + dx[k]
                    y1 = j + dy[k]
                    if x1 >= 0 and x1 < n and y1 >= 0 and y1 < m and vs[x1][y1] == False:
                        res += a[x1][y1]
                        vs[x1][y1] = True
    
    print(res)