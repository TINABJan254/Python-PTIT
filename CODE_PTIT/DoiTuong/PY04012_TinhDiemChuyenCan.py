class SinhVien:
    def __init__(self, id, ten, lop):
        self.id = id
        self.ten = ten
        self.lop = lop
    
    def tinhDiemCc(self, s):
        self.cc = 10
        for i in range(0, len(s)):
            if s[i] == 'm': self.cc -= 1
            elif s[i] == 'v': self.cc -= 2
        if self.cc < 0: self.cc = 0

    def ghiChu(self):
        if self.cc == 0: return 'KDDK'
        return ''

    def __str__(self):
        return self.id + ' ' + self.ten + ' ' + self.lop + ' ' + str(self.cc) + ' ' + self.ghiChu()

#main
n = int(input())
listSinhVien = []
for i in range(n):
    listSinhVien.append(SinhVien(input(), input(), input()))

for i in range(n):
    msv, ds = input().split()
    for sinhVien in listSinhVien:
        if sinhVien.id == msv:
            sinhVien.tinhDiemCc(ds)

for sinhVien in listSinhVien:
    print(sinhVien)


