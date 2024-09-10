def check(n):
    if n[len(n) - 2] != '8' or n[len(n) - 1] != '6':
        return False
    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        n = input()
        if check(n):
            print('YES')
        else:
            print('NO')