from functools import cmp_to_key

def cmp(x, y):
    if x[1] != y[1]:
        return y[1] - x[1]
    else:
        return x[0] - y[0]
    

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    d = dict()
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    res = list(d.items())
    res.sort(key = cmp_to_key(cmp))
    i = 1
    while i < len(res) and res[i][1] == res[i - 1][1]: 
        i += 1 
    if i == len(res): 
        print("NONE")
    else:
        print(res[i][0])