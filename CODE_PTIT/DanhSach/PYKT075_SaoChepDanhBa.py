from functools import cmp_to_key


class DanhBa:
    def __init__(self, ngay, ten, sdt):
        self.ngay = list(ngay.split())[-1]
        self.ten = ten
        self.sdt = sdt
    
    def __str__(self):
        return f'{self.ten}: {self.sdt} {self.ngay}'
    
def cmp(a, b):
    t1 = list(a.ten.split())
    t2 = list(b.ten.split())
    if t1[-1] < t2[-1]:
        return -1
    if t1[-1] > t2[-1]:
        return 1
    if t1[:len(t1)-1] < t2[:len(t2)-1]:
        return -1
    return 1

#main
with open('SOTAY.txt', 'r') as file_object:
    a = file_object.readlines()    

a = [line.strip() for line in a]

listDanhBa = []
i = 0
while i < len(a):
    d = a[i]
    i += 1
    while i < len(a) and a[i][:4:] != 'Ngay':
        ten = a[i]
        i += 1
        sdt = a[i]
        i += 1
        listDanhBa.append(DanhBa(d, ten, sdt))

listDanhBa.sort(key = cmp_to_key(cmp))

with open('DIENTHOAI.txt', 'w') as out:
    for x in listDanhBa:
        out.write(f"{x}\n")  # Ghi thêm \n để xuống dòng
