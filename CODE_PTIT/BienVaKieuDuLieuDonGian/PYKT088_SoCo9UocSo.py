import math

def countNumber(n):
    up_bound = int(n ** (0.5))
    prime = [i for i in range(0, up_bound + 1)]
    for i in range(2, math.isqrt(up_bound) + 1):
        if prime[i] == i:
            for j in range(i * i, up_bound + 1, i):
                prime[j] = i
    
    res = 0
    for i in range(2, up_bound + 1):
        p = prime[i] #ước nt nhỏ nhất của i
        q = i // p
        q = prime[q] # ước nt nhỏ nhất của i / p
        if p * q == i and q != 1 and p != q: # th p^2 * q^2 (xét p*q)
            res += 1
        elif prime[i] == i: # th p^8
            if (i ** 8 <= n):
                res += 1
    return res


if __name__ == '__main__':
    n = int(input())
    print(countNumber(n))


'''
n = p1^e1 * p2^e2 * .... * pk^ek
tổng ước của n: T = (e1+1) * (e2+1) * (e3+1) *...*(ek+1)

=> số có 9 ước sẽ có T = (e1+1) * (e2+1) * (e3+1) *...*(ek+1) = 9
   xét tích các số bằng 9:
    9 * 1 = 9
        tương ứng với k = 1; tức n = p1^e1
        => e1 + 1 = 9
        => e1 = 8
        => n có dạng p^8 (p là snt)
    3 * 3 = 9
        tương ứng k = 2;     tức n = p1^e1 + p2^e2
        => (e1 + 1) * (e2 + 1) = 3 * 3
        => e1 = 2, e2 = 2
        => n có dạng p^2 * q^2 (p, q là snt)
   => vậy chỉ có n = p^8 hoặc p1^2 * q^2

ta chỉ sàng đến căn n vì p^2 * q^2 <= n hay (p*q)^2 = n
    nên chỉ cần sàng đến căn n để lấy số lượng (p*q) là đủ
bước lặp để tìm p, q:
    với 1 số i: ta sẽ đi kiểm tra có nằm trong 2 dạng kể trên hay ko (ở đây với trường hợp p^2*q^2 ta đi xét p*q là đc)
      - với dạng p^8: thì chỉ cần kiểm tra số đó là snt, và mũ 8 lên <= n
      - với dạng p^2*q^2 (đi xét p*q):
        p = prime[i]: ước snt nhỏ nhất của i
        q = i // p
        q = prime[q]
        vì p là ước snt nhỏ nhất của i rồi, mà muốn i có dạng p*q (với p, q là snt)
         thì q cũng phải chính là snt luôn (nên mới có câu q = prime[q], vì nếu q ko phải là snt thì 
         q != prime[q] nên kquả p*q != i)
        thêm nữa là đkiện q != 1 để loại riêng trường hợp i chính là snt (sẽ xét riêng ở p^8) vì nếu i
            là snt thì ko thể nào có hai ước được
        và điều kiện nữa là p, q phân biệt
        




'''