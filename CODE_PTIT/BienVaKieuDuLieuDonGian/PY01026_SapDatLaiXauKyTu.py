def check(s1, s2):
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    return s1 == s2

if __name__ == '__main__':
    for i in range(0, int(input())):
        s1 = input()
        s2 = input()
        print('Test ' + str(i + 1) + ':', end = ' ')
        if check(s1, s2):
            print('YES')
        else:
            print('NO')