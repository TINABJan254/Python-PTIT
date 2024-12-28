n = int(input())
a = list(map(int, input().split()))

ans, cnt, maxE = 0, 0, max(a)
a.append(-1)
for i in range(0, len(a)):
    if a[i] == maxE:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
print(ans)

#Đi tìm dãy con liên tiếp các ptử bằng max(a)