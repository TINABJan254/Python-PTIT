def check(s):
    for i in range(2, len(s), 2):
        if s[i] != s[i - 2]:
            return False
    for i in range(3, len(s), 2):
        if s[i] != s[i - 2]:
            return False;
    return True;

if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")