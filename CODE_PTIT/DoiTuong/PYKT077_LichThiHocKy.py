from datetime import datetime
from functools import cmp_to_key


class MonHoc:
    def __init__(self, maMH, tenMH):
        self.maMH = maMH
        self.tenMH = tenMH
    
    def __str__(self):
        return f'{self.maMH} {self.tenMH}'
    
class CaThi:
    def __init__(self, maCT, monHoc, ngayThi, gioThi, nhomThi):
        self.maCT = maCT
        self.monHoc = monHoc
        self.ngayThi = datetime.strptime(ngayThi.strip(), "%d/%m/%Y")
        self.gioThi = datetime.strptime(gioThi.strip(), "%H:%M")
        self.nhomThi = nhomThi
    
    def __str__(self):
        return f'{self.maCT} {self.monHoc} {self.ngayThi.strftime("%d/%m/%Y")} {self.gioThi.strftime("%H:%M")} {self.nhomThi}'

def cmp(a, b):
    if a.ngayThi < b.ngayThi: return -1
    if a.ngayThi > b.ngayThi: return 1
    if a.gioThi < b.gioThi: return -1
    if a.gioThi > b.gioThi: return 1
    if a.monHoc.maMH < b.monHoc.maMH: return -1
    return 1

#main
n, m = map(int, input().split())
listMonHoc = []
for i in range(n):
    listMonHoc.append(MonHoc(input(), input()))

listCaThi = []
for i in range(m):
    maMH, ngayThi, gioThi, nhomThi = input().split()
    monHoc = None
    for mh in listMonHoc:
        if mh.maMH == maMH: 
            monHoc = mh
            break
    
    listCaThi.append(CaThi(f'T{(i+1):03d}', monHoc, ngayThi, gioThi, nhomThi))

listCaThi.sort(key = cmp_to_key(cmp))

for caThi in listCaThi:
    print(caThi)
