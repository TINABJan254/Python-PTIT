def check(s):
    for i in range(0, len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        s = input()
        if check(s): print('YES')
        else: print('NO')
            