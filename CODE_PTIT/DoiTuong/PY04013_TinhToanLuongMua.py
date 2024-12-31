class Tram:
    def __init__(self, maTram, tenTram, batDau, ketThuc, luongMua, gioMua):
        self.maTram = maTram
        self.tenTram = tenTram
        self.batDau = batDau
        self.ketThuc = ketThuc
        self.luongMua = luongMua
        self.gioMua = gioMua
    
    def luongMuaTB(self):
        return self.luongMua / self.gioMua

    def __str__(self):
        return self.maTram + " " + self.tenTram + " " + f'{self.luongMuaTB():.2f}'
    
#main
n = int(input())
listTram = []
s = set()
cnt = 1
for i in range(0, n):
    tenTram = input()
    batDau = input()
    ketThuc = input()
    luongMua = int(input())
    h1, m1 = map(int, batDau.split(":"))
    h2, m2 = map(int, ketThuc.split(":"))
    thoiGian = (h2 * 60 + m2 - h1 * 60 - m1) / 60.0
    if tenTram not in s:
        maTram = f'T{(cnt):02d}'
        tram = Tram(maTram, tenTram, batDau, ketThuc, luongMua, thoiGian)
        listTram.append(tram)
        cnt += 1
        s.add(tenTram)
    else:
        for x in listTram:
            if x.tenTram == tenTram:
                x.luongMua += luongMua
                x.gioMua += thoiGian
                break
    
for x in listTram:
    print(x)
            
