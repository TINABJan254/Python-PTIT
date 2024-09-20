def check(s):
    a = list(s.split('.'))
    if len(a) != 4: return False
    for i in range(0, len(a)):
        if  (not a[i].isnumeric()) or a[i] > '255':
            return False
    return True

if __name__ == '__main__':
    for _ in range(0, int(input())):
        s = input()
        if check(s):
            print('YES')
        else: 
            print('NO')