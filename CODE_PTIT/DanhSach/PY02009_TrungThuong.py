if __name__ == '__main__':
    for _ in range(0, int(input())):
        n = int(input())
        fre = [0] * 1005
        for i in range(0, n):
            x = int(input())
            fre[x] += 1
        
        res = -1
        maxFre = -1
        for i in range(0, 1005):
            if fre[i] > maxFre:
                maxFre = fre[i]
                res = i
        
        print(res)