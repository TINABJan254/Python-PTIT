from datetime import datetime
from functools import cmp_to_key


class CuaRo:
    def __init__(self, ten, donVi, tgianDen):
        self.ten = ten.strip()
        self.donVi = donVi.strip()
        self.tgianDen = datetime.strptime(tgianDen.strip(), "%H:%M")
        self.taoMa()
    
    def taoMa(self):
        tmp = (self.donVi + ' ' + self.ten).split()
        self.id = ''
        for x in tmp:
            self.id += x[0].upper()

    def vanToc(self):
        t = (self.tgianDen - datetime.strptime("06:00", "%H:%M")).total_seconds() / 3600
        return round(120 / t)
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.donVi} {self.vanToc()} Km/h'

def cmp(a, b):
    return (a.tgianDen - b.tgianDen).total_seconds()
    # không sort theo vận tốc vì vận tốc đã được làm tròn rồi

#main
n = int(input())
a = []
for i in range(n):
    a.append(CuaRo(input(), input(), input()))

a.sort(key = cmp_to_key(cmp))
for x in a:
    print(x)

'''
3
Tran Vu Minh
Ha Noi
8:30
Vu Ngoc Hoang
Hoa Binh
8:20
Pham Dinh Tan
An Giang
8:45  
'''