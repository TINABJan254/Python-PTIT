for _ in range(0, int(input())):
    n = int(input())
    k = 2
    res = 0
    while ((k * (k - 1) // 2) <= n):
        s = n - k * (k - 1) // 2
        if s > 0 and s % k == 0:
            res += 1
        k += 1
    print(res)
'''
tổng 1 dãy liên tiếp k ptử bằng n có dạng:
    x + (x + 1) + ... + (x - k + 1)
    = (x + x + .. + x) + (0 + 1 + .. + k - 1)
    = kx + k*(k-1)/2
    vậy:
    n = kx + k*(k-1) / 2
    <=> kx = n - k*(k-1) / 2
        kx = s (với: x > 0)
    điều kiện:
        1. kx > 0 
         hay s > 0
        2. s % k == 0 (vì x là 1 số nguyên dương)
    giá trị k:
        k chạy từ 2 -> k*(k-1) / 2 <= n
'''
