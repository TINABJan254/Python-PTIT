from datetime import date, datetime
from functools import cmp_to_key

class HoaDon:
    def __init__(self, id, tenKH, soPhong, ngayNhan, ngayTra, tienPhatSinh):
        self.id = id
        self.tenKH = tenKH.strip()
        self.soPhong = soPhong.strip()
        self.ngayNhan = datetime.strptime(ngayNhan.strip(), "%d/%m/%Y").date()
        self.ngayTra = datetime.strptime(ngayTra.strip(), "%d/%m/%Y").date()
        self.tienPhatSinh = tienPhatSinh
    
    def ngayO(self):
        return (self.ngayTra - self.ngayNhan).days + 1
    
    def thanhTien(self):
        if self.soPhong[0] == '1':
            return 25 * self.ngayO() + self.tienPhatSinh
        if self.soPhong[0] == '2':
            return 34 * self.ngayO() + self.tienPhatSinh
        if self.soPhong[0] == '3':
            return 50 * self.ngayO() + self.tienPhatSinh
        return 80 * self.ngayO() + self.tienPhatSinh
    
    def __str__(self):
        return self.id + ' ' + self.tenKH + ' ' + self.soPhong + ' ' + str(self.ngayO()) + ' ' + str(self.thanhTien())
    
def cmp(a, b):
    return b.thanhTien() - a.thanhTien()

#main
n = int(input())
a = []
for i in range(n):
    a.append(HoaDon(f'KH{(i + 1):02d}', input(), input(), input(), input(), int(input())))

a.sort(key = cmp_to_key(cmp))
for x in a:
    print(x)

'''
3
Huynh Van Thanh   
103 
05/06/2010   
05/06/2010   
15
Le Duc Cong  
106 
08/03/2010   
01/05/2010   
220
Tran Thi Bich Tuyen   
207 
10/04/2010   
21/04/2010   
96
'''