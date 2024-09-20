n = int(input())
a = list(map(int, input().split()))

res = 0
for i in range(1, len(a)):
    if a[i] != a[i - 1]:
        res += 1
print(res)