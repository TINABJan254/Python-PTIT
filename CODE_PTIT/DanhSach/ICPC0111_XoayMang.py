for _ in range(0, int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    print(*a[d::], sep = ' ', *a[:d:])