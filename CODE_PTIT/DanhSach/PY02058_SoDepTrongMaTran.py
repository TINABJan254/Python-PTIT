if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(0, n):
        a.append(list(map(int, input().split())))
    
    maxE = -1
    minE = 100000
    for x in a:
        maxE = max(maxE, max(x))
        minE = min(minE, min(x))
    
    found = False
    for i in range(0, n):
        for j in range(0, m):
            if a[i][j] == maxE - minE:
                if not found: print(maxE - minE)
                print(f'Vi tri [{i}][{j}]')
                found = True

    if not found: print('NOT FOUND')