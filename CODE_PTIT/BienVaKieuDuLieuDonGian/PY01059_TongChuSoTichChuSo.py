if __name__ == '__main__':
    for _ in range(0, int(input())):
        n = input()
        chan = 0
        le = 1
        found = False
        for i in range(0, len(n)):
            if i % 2 == 0:
                chan += int(n[i])
            else:
                if n[i] != '0':
                    found = True
                    le *= int(n[i])
        
        print(chan, end = ' ')
        if (found): print(le)
        else: print('0')