def check(s):
    if ("6" not in s) or ("888" in s):
        return False
    for c in s:
        if c != '6' and c != '8':
            return False
    return True

if __name__ == '__main__':
    s = input()
    if check(s):
        print('YES')
    else:
        print('NO')