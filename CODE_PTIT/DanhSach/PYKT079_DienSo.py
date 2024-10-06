for _ in range(0, int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = [0] * 1005
    maxE, minE = max(a), min(a)
    for i in range(0, len(a)):
        d[a[i]] += 1
    
    res = 0
    for i in range(minE, maxE + 1):
        if d[i] == 0:
            res += 1
    print(res)