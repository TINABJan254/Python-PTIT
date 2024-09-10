for _ in range(0, int(input())):
    n = input()
    res = 1
    for c in n:
        if c != '0': res *= int(c)
    print(res)