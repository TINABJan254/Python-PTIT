for _ in range(0, int(input())):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    d1 = dict()
    d2 = dict()
    d3 = dict()

    for x in a:
        if x in d1:
            d1[x] += 1
        else:
            d1[x] = 1
    
    for x in b:
        if x in d2:
            d2[x] += 1
        else:
            d2[x] = 1
    
    for x in c:
        if x in d3:
            d3[x] += 1
        else:
            d3[x] = 1
    
    res = []
    for x in a:
        if x in d2 and d2[x] > 0 and x in d3 and d3[x] > 0:
            res.append(x)
            d2[x] -= 1
            d3[x] -= 1
    
    if len(res) == 0:
        print('NO')
    else:
        print(*res)