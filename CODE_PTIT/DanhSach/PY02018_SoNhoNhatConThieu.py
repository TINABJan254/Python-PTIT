n = int(input())
a = list(map(int, input().split()))

d = [0] * 30005
maxE = -1
for x in a:
    d[x] += 1
    maxE = max(x, maxE)

for i in range(1, maxE + 2):
    if d[i] == 0:
        print(i)
        break
