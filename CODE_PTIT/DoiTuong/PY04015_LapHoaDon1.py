from functools import cmp_to_key


class KhachHang:
    def __init__(self, maKH, tenKH, soCu, soMoi):
        self.maKH = maKH
        self.tenKH = tenKH
        self.soCu = soCu
        self.soMoi = soMoi
    
    def soDien(self):
        return self.soMoi - self.soCu
    
    def soTien(self):
        k = self.soDien()
        if k > 100:
            tmp = 50 * 250 + (k - 100) * 200
            return round(tmp * 105.0 / 100) 
        if k > 50:
            tmp = 50 * 100 + (k - 50) * 150
            return round(tmp * 103.0 / 100)
        return round(k * 100 * 102.0 / 100)

    def __str__(self):
        return self.maKH + " " + self.tenKH + " " + f'{self.soTien():.0f}'

def cmp(a, b):
    if a.soTien() < b.soTien(): return 1
    return -1
    
#main
n = int(input())
listKhachHang = []
for i in range(n):
    listKhachHang.append(KhachHang(f'KH{(i + 1):02d}', input(), int(input()), int(input())))

listKhachHang.sort(key = cmp_to_key(cmp))

for khachHang in listKhachHang:
    print(khachHang)

'''
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
'''