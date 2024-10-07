def trans(s):
    n = 0
    for x in s:
        n += ord(x) - ord('0')
    return str(n)

if __name__ == '__main__':    
    n = input()
    if len(n) == 1:
        print(1)
    else:
        cnt = 0
        while len(n) > 1:
            n = trans(n)
            cnt += 1
        print(cnt)