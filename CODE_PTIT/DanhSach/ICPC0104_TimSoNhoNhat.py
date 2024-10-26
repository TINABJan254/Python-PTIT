if __name__ == '__main__':
    for _ in range(0, int(input())):
        s = input()
        r = ""
        for c in s:
            if c.isdigit():
                r += c
            else:
                r += ' '
        
        a = list(map(int, r.split()))
        res = 99999999
        for x in a:
            res = min(res, x)
        print(res)