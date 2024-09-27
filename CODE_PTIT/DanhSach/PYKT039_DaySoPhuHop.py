def check(a, b):
    a.sort()
    b.sort()
    for i in range(0, n):
        if a[i] > b[i]:
            return False
    return True

for _ in range(0, int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    if check(a, b):
        print('YES')
    else:
        print('NO')