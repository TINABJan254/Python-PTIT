def rotate(a, b):
    if (len(a) != len(b)):
        return -1
    s = a
    for i in range(0, len(a) + 1):
        if s == b:
            return i
        s = s[1::] + s[0]
    return -1

def solve(a):
    ans = 10000000
    for x in a:
        cnt = 0
        for y in a:
            tmp = rotate(y, x)
            if tmp == -1:
                return -1
            cnt += tmp
        ans = min(ans, cnt)
    return ans

if __name__ == '__main__':
    a = []
    for _ in range(0, int(input())):
        a.append(input())
    print(solve(a))