for _ in range(0, int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    d = {}
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    
    for x in d:
        if d[x] % 2 != 0:
            print(x)
            break

