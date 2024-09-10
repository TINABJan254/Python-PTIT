if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        s = input()
        s += '#'
        cnt = 1
        for i in range(0, len(s) - 1):
            if s[i] != s[i + 1]:
                print(cnt, s[i], sep = '', end = '')
                cnt = 1
            else:
                cnt += 1
        print()
