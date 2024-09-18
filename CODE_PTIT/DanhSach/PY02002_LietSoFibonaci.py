if __name__ == '__main__':
    f = [0, 1, 1, 2]
    for i in range(4, 94):
        f.append(0)
        f[i] = f[i - 1] + f[i - 2]
    
    for _ in range(0, int(input())):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            print(f[i], end = ' ')
        print()