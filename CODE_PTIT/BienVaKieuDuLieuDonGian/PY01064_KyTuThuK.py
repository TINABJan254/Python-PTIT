F = [0] * 93
R = []

def init():
    F[1] = 1
    for i in range(2, 27):
        F[i] = F[i - 1] * 2 + 1
    
    R.append('A')
    for i in range(1, 26):
        R.append(chr(ord(R[i - 1]) + 1))

def find(n, k):
    if n == 1:
        return 'A'
    if k == F[n] // 2 + 1:
        return R[n - 1]
    if k <= F[n - 1]:
        return find(n - 1, k)
    return find(n - 1, k - F[n - 1] - 1)

if __name__ == '__main__':
    init()
    for _ in range(0, int(input())):
        n, k = map(int, input().split())
        print(find(n, k))
