from datetime import datetime
from functools import cmp_to_key


class CaThi:
    def __init__(self, maCT, ngayThi, gioThi, phongThi):
        self.maCT = maCT
        self.ngayThi = datetime.strptime(ngayThi, "%d/%m/%Y")
        self.gioThi = datetime.strptime(gioThi, "%H:%M")
        self.phongThi = phongThi
    
    def __str__(self):
        return f'{self.maCT} {self.ngayThi.strftime("%d/%m/%Y")} {self.gioThi.strftime("%H:%M")} {self.phongThi}'

def cmp(a, b):
    if a.ngayThi < b.ngayThi: return -1
    if a.ngayThi > b.ngayThi: return 1
    if a.gioThi < b.gioThi: return -1
    if a.gioThi > b.gioThi: return 1
    return 1

# main
listCaThi = []
with open('CODE_PTIT/DanhSach/CATHI.in', 'r') as fo:
    n = int(fo.readline().strip())
    for i in range(n):
        listCaThi.append(CaThi(f'C{(i+1):03d}', fo.readline().strip(), fo.readline().strip(), fo.readline().strip()))

listCaThi.sort(key = cmp_to_key(cmp))

for caThi in listCaThi:
    print(caThi)