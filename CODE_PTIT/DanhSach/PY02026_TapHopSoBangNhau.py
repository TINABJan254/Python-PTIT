def check(a, b):
    if len(a) != len(b):
        return False
    for i in range(0, len(a)):
        if a[i] != b[i]:
            return False
    return True

if __name__ == '__main__':
    n, m = map(int, input().split())

    a = sorted(set(list(map(int, input().split()))))
    b = sorted(set(list(map(int, input().split()))))

    if check(a, b):
        print('YES')
    else:
        print('NO')