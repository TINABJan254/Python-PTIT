n = int(input())
a = list(map(float, input().split()))

a.sort()
L, R = 0, n - 1
while L < n - 2 and a[L] == a[L + 1]:
    L += 1
while R >= 1 and a[R] == a[R - 1]:
    R -= 1
    
res = 0
for i in range(L + 1, R):
    res += a[i]

print(round(res / (R - L - 1), 2))