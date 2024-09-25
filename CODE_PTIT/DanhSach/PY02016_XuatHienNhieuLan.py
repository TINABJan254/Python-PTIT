if __name__ == '__main__':
    for _ in range(0, int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        fre = {}
        for x in a:
            if x in fre:
                fre[x] += 1
            else:
                fre[x] = 1
        maxE = -1
        res = 0
        for x in fre:
            if fre[x] > maxE:
                maxE = fre[x]
                res = x
            elif fre[x] == maxE:
                if x < res:
                    res = x
        
        if maxE > n // 2:
            print(res)
        else:
            print('NO')
