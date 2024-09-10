if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        s = input()
        i = 0
        while i < len(s):
            c = s[i]
            fre = int(s[i + 1])
            for _ in range(0, fre): print(c, sep = '', end = '')
            i += 2
        print()
            
