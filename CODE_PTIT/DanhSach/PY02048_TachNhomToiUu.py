n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

if n == 0: print(0)
else:
    cnt = 1
    for i in range(1, len(a)):
        if a[i] - a[i - 1] > k:
            cnt += 1
    print(cnt)