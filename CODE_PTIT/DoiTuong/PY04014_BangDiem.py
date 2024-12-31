from functools import cmp_to_key

def custom_round(number, decimal_places):
  factor = 10 ** decimal_places
  rounded_number = int(number * factor + 0.5) / factor
  return rounded_number

class SinhVien:
    def __init__(self, maSV, ten, diem):
        self.maSV = maSV
        self.ten = ten
        self.diem = diem
    
    def diemTB(self):
        t = sum(self.diem)
        t += self.diem[0] + self.diem[1]
        return custom_round(t/12, 1)

    def xepLoai(self):
        tb = self.diemTB()
        if tb >= 9.0: return 'XUAT SAC'
        if tb >= 8.0: return 'GIOI'
        if tb >= 7.0: return 'KHA'
        if tb >= 5.0: return 'TB'
        return 'YEU'

    def __str__(self):
        return self.maSV + " " + self.ten + " " + f'{self.diemTB():.1f}' + " " + self.xepLoai()

def cmp(a, b):
    if a.diemTB() > b.diemTB(): return -1
    if a.diemTB() < b.diemTB(): return 1
    if a.maSV < b.maSV: return -1
    return 1

#main
n = int(input())
listSinhVien = []
for i in range(n):
    listSinhVien.append(SinhVien(f'HS{(i+1):02d}', input(), list(map(float, input().split()))))

listSinhVien.sort(key = cmp_to_key(cmp))
for sinhVien in listSinhVien:
    print(sinhVien)

'''
3
Luu Thuy Nhi
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
'''
